from website import start_app
app = start_app()

# starting our app - Development
if __name__ == '__main__':
    app.run(debug=True)

# starting our app - Deployment / Production
# if __name__ == '__main__':
#     app.run()