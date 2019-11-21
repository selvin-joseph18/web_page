import connexion


# Create the application instance
app = connexion.App(__name__, specification_dir='end_point/')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
