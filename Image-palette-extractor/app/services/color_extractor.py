from PIL import Image


THUMBNAIL_WIDTH: int = 150
THUMBNAIL_HEIGHT: int = 150
THUMBNAIL_SIZE: tuple[int, int] = (THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT)
DEFAULT_NUM_COLORS: int = 10
MIN_COLORS: int = 1

def extract_dominant_colors(image: Image.Image, num_colors: int = DEFAULT_NUM_COLORS) -> list[str]:
    """Extract the top N dominant HEX colors from a Pillow Image object.

    Args:
        image: A valid PIL.Image.Image instance.
        num_colors: Maximum number of dominant colors to return. Defaults to 10.

    Returns:
        A list of uppercase HEX color strings (e.g., ['#FF5733', ...]) sorted
        from most frequent to least frequent.

    Raises:
        ValueError: If image is None or num_colors is less than 1.
    """
    if image is None:
        raise ValueError("An image object must be provided.")
    if num_colors < MIN_COLORS:
        raise ValueError(f"num_colors must be at least {MIN_COLORS}.")

    #Normalize to 3-channel RGB so RGBA, L, or P images behave identically
    rgb_image = image.convert("RGB")

    #Downscale in-place on the new RGB copy for fast processing
    rgb_image.thumbnail(THUMBNAIL_SIZE)

    #Quantize into N distinct color buckets (returns a 'P' mode image)
    quantized_image = rgb_image.quantize(colors=num_colors)

    #Fetch (pixel_count, palette_index) pairs and sort highest count first
    color_counts = quantized_image.getcolors(maxcolors=num_colors)
    palette = quantized_image.getpalette()

    if not color_counts or not palette:
        return []

    sorted_colors = sorted(color_counts, key=lambda item: item[0], reverse=True)

    #Map each palette index to its [R, G, B] slice and format as HEX
    hex_colors: list[str] = []
    for _count, color_index in sorted_colors:
        start = color_index * 3
        r, g, b = palette[start : start + 3]
        hex_colors.append(f"#{r:02X}{g:02X}{b:02X}")

    return hex_colors


if __name__ == "__main__":
    # Quick local sanity check before integrating with Flask
    sample_path = "path/to/your/sample_image.jpg"
    with Image.open(sample_path) as test_img:
        dominant_palette = extract_dominant_colors(test_img, num_colors=10)
        print("Extracted HEX Palette:", dominant_palette)