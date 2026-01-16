def analyze_emotions_realtime():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Cannot open webcam")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret or frame is None or frame.size == 0:
            print("Failed to capture frame")
            break
            
        # Analyze every few frames to improve performance
        try:
            # Make a copy of the frame to avoid modification issues
            img_for_analysis = frame.copy()
            
            # Check if the frame is valid before analysis
            if img_for_analysis is not None and img_for_analysis.size > 0:
                analysis = DeepFace.analyze(img_path=img_for_analysis, 
                                          actions=['emotion'],
                                          enforce_detection=False,
                                          detector_backend='opencv')
                
                if isinstance(analysis, list):
                    analysis = analysis[0]
                    
                dominant_emotion = analysis['dominant_emotion']
                
                # Display the result on the frame
                cv2.putText(frame, f"Emotion: {dominant_emotion}", 
                           (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                           0.8, (0, 255, 0), 2)
        except Exception as e:
            # Print the specific error for debugging
            print(f"Analysis error: {e}")
            pass
        
        # Display the frame
        cv2.imshow('Emotion Analysis', frame)
        
        # Break loop with 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Run real-time analysis
analyze_emotions_realtime()
