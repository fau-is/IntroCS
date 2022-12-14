# Action Execution
In this example, you find three files. A program in _main.py_, the controller in _controller.py_ and different actions to perform with an examplary file in _actions.py_

## something.txt
This is just an examplary file, that you can use to try out the file actions.

## Controller.py
The controller executes actions and provides a protocol for all executed actions.
It determines whether an action was successful or not.

## Actions.py
For every file action, one class was implemented. Each class has two properties:
* _src\_path_ (File to be handled)
* _target\_path_ (New file name, or copy destination)

In addition, all actions implement the method _do\_action_() which actually executes the action's purpose.

As you can see, _DeleteAction_ only uses the src_path and the controller can still make use of the do_action() function, as it represents a stable interface for all subclasses.

## main.py
You can either execute _main.py_ as is, or you change it and try it out a bit on your own.
