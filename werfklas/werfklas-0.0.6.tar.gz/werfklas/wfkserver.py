from waitress import serve
import werfklas
serve(werfklas.app, host='0.0.0.0', port=8080)
