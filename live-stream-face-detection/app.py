
from flask import Flask, render_template, Response
from camera_openpose import camera_stream

app = Flask(__name__)


@app.route('/')
def index():
    print('get-----')
    """Video streaming home page."""
    return render_template('index.html')


def gen_frame():
    print('gen')
    """Video streaming generator function."""
    while True:
        frame = camera_stream() # bytes的拼接
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') # concate frame one by one and show result


@app.route('/video_feed')
def video_feed():
    print('get frame')
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0',threaded=True,port=9000)
