
from ultralytics import YOLO
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="YOLO11 Road Accident Detection"
    )

    parser.add_argument(
        "--source",
        required=True,
        help="Path to an image, video, or webcam source"
    )

    parser.add_argument(
        "--conf",
        type=float,
        default=0.50,
        help="Confidence threshold (default: 0.50)"
    )

    parser.add_argument(
        "--output",
        default="runs/detect",
        help="Output directory"
    )

    args = parser.parse_args()

    model_path = Path(__file__).parent / "models" / "accident_detector_V1_best.pt"

    if not model_path.exists():
        raise FileNotFoundError(
            f"Model not found: {model_path}"
        )

    print("Loading Accident Detection Model...")
    model = YOLO(str(model_path))

    print(f"Source: {args.source}")
    print(f"Confidence threshold: {args.conf}")

    results = model.predict(
        source=args.source,
        conf=args.conf,
        save=True,
        project=args.output,
        name="prediction",
        exist_ok=True
    )

    print("\n✅ Detection completed!")
    print(f"📁 Results saved to: {args.output}/prediction")


if __name__ == "__main__":
    main()
