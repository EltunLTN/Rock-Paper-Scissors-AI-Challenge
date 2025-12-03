from flask import Flask, render_template, Response, jsonify
import cv2
import mediapipe as mp
import random

app = Flask(__name__)

# MediaPipe əl tanıma
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Oyun dəyişənləri
user_score = 0
computer_score = 0
game_over = False

def detect_gesture(landmarks):
    fingers = []

    tip_ids = [4, 8, 12, 16, 20]  # baş barmaq + 4 barmaq ucu

    # Baş barmaq (x mövqeyinə görə)
    if landmarks[tip_ids[0]].x < landmarks[tip_ids[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Digər barmaqlar (y mövqeyinə görə)
    for id in range(1, 5):
        if landmarks[tip_ids[id]].y < landmarks[tip_ids[id] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    # Jestləri müəyyənləşdir
    if fingers == [0, 0, 0, 0, 0]:
        return "rock"
    elif fingers == [1, 1, 1, 1, 1]:
        return "paper"
    elif fingers == [0, 1, 1, 0, 0]:
        return "scissors"
    else:
        return "unknown"

def play_round(user_move):
    global user_score, computer_score, game_over

    moves = ["rock", "paper", "scissors"]
    computer_move = random.choice(moves)

    winner = "draw"
    if user_move != "unknown":
        if (user_move == "rock" and computer_move == "scissors") or \
           (user_move == "paper" and computer_move == "rock") or \
           (user_move == "scissors" and computer_move == "paper"):
            user_score += 1
            winner = "user"
        elif user_move != computer_move:
            computer_score += 1
            winner = "computer"

    if user_score >= 5 or computer_score >= 5:
        game_over = True

    return user_move, computer_move, winner

def generate_frames():
    global user_score, computer_score, game_over
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # BGR → RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                gesture = detect_gesture(hand_landmarks.landmark)
                user_move, comp_move, winner = play_round(gesture)

                cv2.putText(frame, f"You: {gesture} | PC: {comp_move}", (10, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.putText(frame, f"Score: {user_score} - {computer_score}", (10, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

                if game_over:
                    cv2.putText(frame, "GAME OVER", (200, 200),
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/reset')
def reset():
    global user_score, computer_score, game_over
    user_score = 0
    computer_score = 0
    game_over = False
    return jsonify({"status": "reset"})

if __name__ == "__main__":
    app.run(debug=True)
