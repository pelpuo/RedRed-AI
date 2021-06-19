from flask import Flask
import os
import torch

# model = torch.hub.load('ultralytics/yolov5', 'yolov5s', classes=1)
# model.load_state_dict(torch.load('website/model.pt')['model'].state_dict())

# model = model.fuse().autoshape()
model = torch.hub.load('ultralytics/yolov5', 'custom', path='website/best_weights.pt')  # default

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secret"
    
    from .views import views
    from .auth import auth
    from .handlers import handlers

    RESULT_FOLDER = os.path.join('static')
    app.config['RESULT_FOLDER'] = RESULT_FOLDER

    model.eval()

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(handlers, url_prefix="/model")

    return app