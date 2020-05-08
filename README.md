<img src="images/curve.gif" alt="curve.gif" width="500" height="500" />

* Install 

** Optional create a virtual env
#+BEGIN_SRC sh
python -m venv venv
source venv/bin/activate
#+END_SRC

** Install requirements
#+BEGIN_SRC sh
pip install -r requirements.txt
#+END_SRC

* Run the app
#+BEGIN_SRC sh
flask run
#+END_SRC

* Setup 

In order to make it works you need to write the code for a few functions:

** load_curve

In =app.py= the function load_curve takes as parameter an =id= and return a 3D curve as 
an iterable of 3-tuples. See examples section for more. 


** Examples   

*** Matlab files loader 

#+BEGIN_SRC python 
  def load_curve(curve_id):
      import scipy.io as sio

      data = sio.loadmat(
          "/path/to/data.mat"
      )
      data = data["curves"]

      return data[:, :, curve_id]
#+END_SRC
