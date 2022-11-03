import os

SECRET_KEY = os.getenv("SKELENGO_DJANGO_SECRET_KEY")
if not SECRET_KEY:
    SECRET_KEY = "$&4a@f6qh5_00(j!#lnsw1far@0c)(@s_r79w6cr$tr_f*0rbb"
