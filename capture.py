
import logging
import re
import time
from pathlib import Path

import cv2


def _sanitize_label(raw: str) -> str:
	label = raw.strip()
	label = re.sub(r"\s+", "_", label)
	label = re.sub(r"[^A-Za-z0-9_-]", "", label)
	return label


def _next_image_index(out_dir: Path, label: str) -> int:
	existing_max = 0
	pattern = re.compile(rf"^{re.escape(label)}(\d+)\.jpg$")
	for p in out_dir.glob(f"{label}*.jpg"):
		m = pattern.match(p.name)
		if not m:
			continue
		try:
			n = int(m.group(1))
		except ValueError:
			continue
		existing_max = max(existing_max, n)
	return existing_max + 1


def main() -> None:
	logging.basicConfig(
		level=logging.INFO,
		format="%(asctime)s | %(levelname)s | %(message)s",
	)

	print("Dataset capture")
	print("- Enter label name (folder name)")
	print("- Enter how many images to capture")
	print("- Press SPACE to save an image")
	print("- Press ESC to quit")
	print()

	raw_label = input("Label/folder name: ")
	label = _sanitize_label(raw_label)
	if not label:
		raise SystemExit("Label is empty/invalid after sanitizing. Try another name.")

	raw_count = input("How many images? ").strip()
	if not raw_count.isdigit() or int(raw_count) <= 0:
		raise SystemExit("Please enter a positive integer for the number of images.")
	target_count = int(raw_count)

	base_dir = Path("dataset")
	out_dir = base_dir / label
	out_dir.mkdir(parents=True, exist_ok=True)

	logging.info("Saving images to: %s", out_dir.resolve())

	start_index = _next_image_index(out_dir, label)
	logging.info("Starting image index at: %d", start_index)

	cap = cv2.VideoCapture(0)
	if not cap.isOpened():
		raise SystemExit("Could not open webcam (device 0).")

	saved = 0
	window_name = "Dataset Capture"

	try:
		while True:
			ok, frame = cap.read()
			if not ok:
				logging.error("Failed to read frame from webcam.")
				break

			# Show a clean preview (no overlay), and keep status in terminal logs.
			cv2.imshow(window_name, frame)
			key = cv2.waitKey(1) & 0xFF

			if key == 27:  # ESC
				logging.info("Exit requested. Saved %d/%d images.", saved, target_count)
				break

			if key == 32:  # SPACE
				if saved >= target_count:
					logging.info("Target reached (%d). Press ESC to exit.", target_count)
					continue

				image_index = start_index + saved
				filename = f"{label}{image_index}.jpg"
				path = out_dir / filename
				ok_write = cv2.imwrite(str(path), frame)
				if not ok_write:
					logging.error("Failed to write image: %s", path)
					continue

				saved += 1
				logging.info("Captured %d/%d -> %s", saved, target_count, path)

				if saved >= target_count:
					logging.info("Done. Captured %d images.", saved)
					# Keep preview open until ESC, but avoid accidental double-capture
					time.sleep(0.2)

	finally:
		cap.release()
		cv2.destroyAllWindows()


if __name__ == "__main__":
	main()
