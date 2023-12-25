import cv2

class FaceProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def preprocess(self):
        try:
            if self.file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
                self.data = cv2.imread(self.file_path)
            elif self.file_path.lower().endswith(('.mp4', '.avi')):
                pass
            else:
                raise ValueError("Unsupported file format. Please provide a valid image (jpg, png) or video (mp4, avi).")
        except Exception as e:
            print(f"Error during preprocessing: {e}")

    def detect(self):
        if self.data is None:
            print("Error during detection: No data to process. Please call preprocess() first.")
            return

        gray = cv2.cvtColor(self.data, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(self.data, (x, y), (x+w, y+h), (255, 0, 0), 2)

    def infer(self):
        # Add your inference logic here
        pass

    def display(self):
        if self.data is None:
            print("Error during display: No data to display. Please call preprocess() first.")
            return

        cv2.imshow('Face Processor', self.data)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


file_path = "1.jpg"
processor = FaceProcessor(file_path)
processor.preprocess()
processor.detect()
processor.display()
