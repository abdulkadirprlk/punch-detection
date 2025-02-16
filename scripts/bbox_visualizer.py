import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image


def visualize_bboxes(image_path, bboxes, title="Bounding Boxes"):
    """
    Visualizes bounding boxes on an image.

    Parameters:
    - image_path (str): Path to the image file.
    - bboxes (list of lists): Bounding boxes as [[x_min, y_min, x_max, y_max], ...].
    - title (str): Title of the plot.

    Returns:
    - None: Displays the image with bounding boxes.
    """
    # Open the image
    image = Image.open(image_path)
    width, height = image.size

    # Create a plot
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(image)
    ax.set_title(title)
    ax.axis("off")

    # Draw each bounding box
    for bbox in bboxes:
        x_min, y_min, x_max, y_max = bbox

        # Calculate width and height of the bounding box
        bbox_width = x_max - x_min
        bbox_height = y_max - y_min

        # Create a rectangle patch
        rect = patches.Rectangle(
            (x_min, y_min), bbox_width, bbox_height,
            linewidth=2, edgecolor='r', facecolor='none'
        )

        # Add the patch to the axes
        ax.add_patch(rect)

    # Show the plot
    plt.show()


if __name__ == "__main__":
    visualize_bboxes(image_path, bboxes, title="Example Bounding Boxes")
