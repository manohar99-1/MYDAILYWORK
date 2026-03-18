from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests

# Load model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


def caption_from_url(image_url):
    """Generate caption for an image from URL"""
    image = Image.open(requests.get(image_url, stream=True).raw).convert("RGB")
    inputs = processor(image, return_tensors="pt")
    output = model.generate(**inputs)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption


def caption_from_file(image_path):
    """Generate caption for a local image file"""
    image = Image.open(image_path).convert("RGB")
    inputs = processor(image, return_tensors="pt")
    output = model.generate(**inputs)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption


def main():
    print("=== Image Captioning AI ===\n")
    print("Choose input type:")
    print("1. Image URL")
    print("2. Local image file path")
    choice = input("\nEnter choice (1 or 2): ").strip()

    if choice == "1":
        url = input("Enter image URL: ").strip()
        print("\nGenerating caption...")
        caption = caption_from_url(url)

    elif choice == "2":
        path = input("Enter image file path: ").strip()
        print("\nGenerating caption...")
        caption = caption_from_file(path)

    else:
        print("Invalid choice.")
        return

    print(f"\nCaption: {caption}")


if __name__ == "__main__":
    main()
