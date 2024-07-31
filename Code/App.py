import cv2


def upscale_image(input_image_path, output_image_path, scale_factor=4):
    # Read the input image
    image = cv2.imread(input_image_path)
    

    # Get the dimensions of the image
    height, width = image.shape[:2]
    
    # Calculate new dimensions
    new_width = width * scale_factor
    new_height = height * scale_factor
    

    # Upscale the image using cv2.resize with INTER_CUBIC interpolation
    upscaled_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
    

    # Save the upscaled image
    cv2.imwrite(output_image_path, upscaled_image)
    print(f"Upscaled image saved to {output_image_path}")

name = "main"                    #this line optinal depend on  your machine
if name == "main":
    input_image_path = 'input.jpg'
    output_image_path = 'upscaled_image.jpg'
    upscale_image(input_image_path, output_image_path)







   
   
    # use img with input.jpg atherws you change your img path value 





