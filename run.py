from dotenv import load_dotenv
load_dotenv()

from backend.app import create_app
app = create_app()

import os
running = os.environ.get('APP_ENV') or 'development'
debug = running == 'development'

if __name__ == '__main__':
  app.run(
    host="0.0.0.0",
    debug=debug,
    port=int(os.environ.get('PORT', 5000))
  )
