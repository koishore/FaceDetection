# FaceDetection

FaceDetection is a python script created for the final Project of Introduction to Machine Learning by Professor Yamuna Shukla at Ashoka University for the Fall 2016 Semester.
<br>
Check out a few results that our code returned in the Samples directory.

## Language(s) and Tool(s) Used

- Python

## Versions

- Python 2.7.10

## Dependencies

- OpenCV v2.4.13

## Authors

- Koishore Roy
- Ujjwal Yadav

## Setup and Initialising (Linux and MacOS)

- Clone this directory into your local system
- Open terminal and navigate to the directory where cloned the repository
- Type "cd FaceDetection" and press Enter
- Run "python takepictures.py"
- When a webcam window opens, press Spacebar to take pictures and Escape to quit
- When you are done taking pictures, navigate to the 'images' directory inside the repository
- You will find all the pictures that you took with rectangles drawn around the faces the program detected
- Alternatively, you can choose to manually check for faces within a picture.
- Run "python face_detectmanual.py"
- You will be prompted to enter a filename without the extension.
- Enter the filename (example: test for test.jpg located in the same directory)
- Incase of a different directory, say myimages/test.png, type 'myimages/test'
- In put the extension of the file when prompted withut a '.' (For example: jpg for a file named test.jpg)
- Press Enter and the picture will have a different rectangle drawn around each face.

## Warning

Be sure to keep backed up copies of your pictures when manually detecting faces in them. The rectangles drawn around the pictures are permanent. FaceDetection does not take any responsibility for tampered and ruined pictures due to the python script.
