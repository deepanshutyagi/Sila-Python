#!flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response
import random, json
from silasdk import App
from silasdk import User
from silasdk import Transaction


app1=App("prod",'26230D5916D1BD6BDB9CF04FAA48123F80BE1B883A61ED94884F0D6A763619F4',"tyagi1.silamoney.eth")

app = Flask(__name__)

@app.route('/')
def output():
	return render_template('index.html', name='Joe')


@app.route('/checkHandle', methods = ['POST'])
def checkHandle():
    data = request.json
    result = json.dumps(User.checkHandle(app1,data))
    return result

@app.route('/register', methods = ['POST'])
def register():
    # read json + reply
    data = request.json
    result = json.dumps(User.register(app1,data))
    return result


@app.route('/requestKyc', methods = ['POST'])
def requestKyc():
    '''SECURITY ALERT
    Never transmit private keys over the network in the request body
    You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
    Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction 
    '''
    data = request.json
    result = json.dumps(User.requestKyc(app1,data,data["private_key"]))
    return result



@app.route('/checkKyc', methods = ['POST'])
def checkKyc():
        '''SECURITY ALERT
        Never transmit private keys over the network in the request body
        You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
        Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction 
        '''
        # read json + reply
        data = request.json
        result = json.dumps(User.checkKyc(app1,data,data["private_key"]))
        return result



@app.route('/linkAccount', methods = ['POST'])
def linkAccount():
    '''SECURITY ALERT
    Never transmit private keys over the network in the request body
    You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
    Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction 
    '''
    data=request.data
    data1=json.loads(data)
    result = json.dumps(User.linkAccount(app1,data1,data1["private_key"]))
    return result


@app.route('/getAccounts', methods = ['POST'])
def getAccounts():
    '''SECURITY ALERT
    Never transmit private keys over the network in the request body
    You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
    Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction 
    '''
    data = request.json
    private_key=data["private_key"]
    result = json.dumps(User.getAccounts(app1,data,private_key))
    return result



@app.route('/getTransactions', methods = ['POST'])
def getTransactions():
    '''SECURITY ALERT
    Never transmit private keys over the network in the request body
    You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
    Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction 
    '''
    data = request.json
    private_key=data["private_key"]
    result = json.dumps(User.getTransactions(app1,data,private_key))
    return result


@app.route('/issueSila', methods = ['POST'])
def issueSila():
    '''SECURITY ALERT
    Never transmit private keys over the network in the request body
    You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
    Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction 
    '''
    data = request.json
    private_key=data["private_key"]
    result = json.dumps(Transaction.issueSila(app1,data,private_key))
    return result


@app.route('/redeemSila', methods = ['POST'])
def redeemSila():
    '''SECURITY ALERT
    Never transmit private keys over the network in the request body
    You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
    Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction 
    '''
    data = request.json
    private_key=data["private_key"]
    result = json.dumps(Transaction.redeemSila(app1,data,private_key))
    return result



@app.route('/transferSila', methods = ['POST'])
def transferSila():
    '''SECURITY ALERT
    Never transmit private keys over the network in the request body
    You see a private key in request body here as this is intended for testing linkaccount and other endpoints locally
    Refer to documentation for how to manage your private keys and how it is used by our sdks locally to sign a transaction 
    '''
    data = request.json
    private_key=data["private_key"]
    result = json.dumps(Transaction.transferSila(app1,data,private_key))
    return result





if __name__ == '__main__':
	# run!
	app.run(debug=True)