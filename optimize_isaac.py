from PIL import Image
import os

imagePath = r'c:\Users\Personal\Desktop\ficgithubsite\ficwebsitetest-main\ficwebsitetest-main\isaac ssenyonga.JPG'

# Get original size
original_size = os.path.getsize(imagePath) / (1024 * 1024)
print(f'Original file size: {original_size:.2f} MB')

# Open image
img = Image.open(imagePath)
print(f'Original dimensions: {img.size}')

# Resize to max 1200px width, maintaining aspect ratio
max_width = 1200
if img.width > max_width:
    ratio = max_width / img.width
    new_height = int(img.height * ratio)
    img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
    print(f'Resized to: {img.size}')

# Save optimized
img.save(imagePath, 'JPEG', quality=85, optimize=True)

# Get new size
new_size = os.path.getsize(imagePath) / (1024 * 1024)
reduction = ((original_size - new_size) / original_size) * 100
print(f'Optimized file size: {new_size:.2f} MB')
print(f'✓ Optimization complete ({reduction:.1f}% reduction)')
