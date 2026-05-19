import base64
import io
from PIL import Image, ImageDraw, ImageFont


def image_bytes_to_data_url(image_bytes: bytes, mime_type: str) -> str:
    return f"data:{mime_type};base64," + base64.b64encode(image_bytes).decode("utf-8")


def build_contact_sheet(items: list[dict], title: str) -> tuple[bytes, str]:
    if not items:
        raise ValueError("No images provided")

    max_w = 1100
    max_h = 620
    pad = 20
    label_h = 40
    header_h = 60
    cols = 1 if len(items) == 1 else 2
    rows = (len(items) + cols - 1) // cols
    cell_w = max_w + pad * 2
    cell_h = max_h + label_h + pad * 2

    sheet = Image.new("RGB", (cols * cell_w, header_h + rows * cell_h), "white")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    draw.text((pad, 20), title[:140], fill="black", font=font)

    for i, item in enumerate(items):
        img = Image.open(io.BytesIO(item["bytes"])).convert("RGB")
        img.thumbnail((max_w, max_h))
        col = i % cols
        row = i // cols
        x = col * cell_w + pad
        y = header_h + row * cell_h + pad
        draw.text((x, y), str(item.get("label", "Screenshot"))[:140], fill="black", font=font)
        frame_y = y + label_h
        bg = Image.new("RGB", (max_w, max_h), "#f2f2f2")
        bg.paste(img, ((max_w - img.width) // 2, (max_h - img.height) // 2))
        sheet.paste(bg, (x, frame_y))
        draw.rectangle([x, frame_y, x + max_w, frame_y + max_h], outline="#cccccc", width=2)

    out = io.BytesIO()
    sheet.save(out, format="JPEG", quality=75, optimize=True)
    return out.getvalue(), "image/jpeg"
