#!/usr/bin/env python
# Abdallah Hassan  Software Produce ok

import os
from flask import Flask, request, render_template, jsonify
from json import dumps
import json 
app = Flask(__name__, static_folder='public', template_folder='templates')


app.secret = os.environ.get('534o5o34o5jpo234oomdfsog')






#ok thanks
@app.route('/send_phone')
def to_contact():
  phone_no = request.args['last_input'].replace(' ','').replace('-','')
  platform = request.args['platform']
  
  if phone_no.replace('+','').isdigit():
    if phone_no[0] == '+':
      phone_no = phone_no
    elif phone_no[:2] == '05':
      phone_no = '+966'+phone_no[1:]
  else:
    if platform == 'telegram':    
      return json.dumps([{
      "type": "messages",
        "content": {
          "text": "Please send vaild phone no",          
          "parse_mode": "html"
        }
      }
      ])
    # else:
      # {"message": {"attachment": {"type": "template", "payload": {"template_type": "button", "text": "", "buttons": [{"title": "", "type": "postback", "payload": 1189}
  
  return json.dumps([{
    "type": "messages",
      "content": {
        "text": "Here",
        "reply_markup": {"inline_keyboard": [[{"text": "Whatsapp", "url": "https://wa.me/"+phone_no}]]}},
        "parse_mode": "html"
      }])


@app.route('/ATriggerVerify.txt')
def ATriggerVerify():
    return render_template('ATriggerVerify.txt')

if __name__ == '__main__':
    app.run()
