import sys
sys.path.insert(1, "./")

from server import server
from controllers import app

if __name__ == "__main__":
    server.run(app)
