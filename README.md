
# Hirst Painting Project

This Python program generates a 10x10 grid painting inspired by the works of Damien Hirst, using the `turtle` graphics library. The program utilizes the `colorgram` module to extract colors from an image, which are then used to create vibrant dots on the canvas.

## Overview

The program creates a grid of colored dots on the screen, simulating the famous dot paintings of Damien Hirst. The user can adjust various constants in the code to modify the size of the dots, the spacing between them, and the overall grid size to create larger or smaller paintings.

## Getting Started

### Prerequisites

- **Python 3.x** must be installed on your system.
- **turtle** and **colorgram.py** libraries are required. You can install them via pip:
  
  ```bash
  pip install colorgram.py
  ```

### Installation

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/0x2V369/hirst-painting-project.git
   cd hirst-painting-project
   ```

2. **Add the Image for Color Extraction**

   The program requires an image file (`image.jpg`) from which colors are extracted. You will need to manually add this image to the root directory of the cloned repository. Ensure the image file is named `image.jpg`.

### Running the Program

Once you have added the required image and installed the necessary dependencies, you can run the program using:

```bash
python hirst_painting_project.py
```

### Adjusting the Painting

The program includes constants for dot size, spacing, and grid size. You can adjust these constants in the code to produce a larger or smaller painting:

- `DOT_SIZE`: The diameter of each dot.
- `SPACING`: The space between each dot.
- `GRID_SIZE`: The number of dots per row and column.

These values can be customized to fit your specific needs.

## Inspiration

This project is inspired by the iconic dot paintings of British artist Damien Hirst. All praise for the artistic inspiration goes to him.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Author

This silent auction program was developed by [0x2V369](https://github.com/0x2V369).