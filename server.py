import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='endpoint/')
app.add_api('swagger.yml')
# Create a URL route in our application for "/"

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
