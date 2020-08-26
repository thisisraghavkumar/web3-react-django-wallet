# Sqlite-Django-React Ethereum Profile
This tool shows the profile of the ethereum address given to it. The profile contains -
* Balance of address
* Transactions made to or from address

When connected to the ethereum network the homepage will show a list of saved contacts of the address selected in metamask.

## Steps of building this project

### 1. Creating the project

We begin by initializing all the folders that we will require for the project and installing the dependencies.

* Creating a python virtual environment and installing dependencies.
```cmd
virtualenv .
Scripts/activate
pip install django django-rest-framework django-cors-headers
```
* Creating a django project and adding apps
```cmd
django-admin startproject wallet
cd wallet
python manage.py startapp api
python manage.py startapp webpage
```
* Creating front end project in the wallet folder
```cmd
npm install create-react-app -g
create-react-app wallet-frontend
npm install web3 axios react-router-dom
```

After this step the project directory structure will look like 

wallet -> wallet, api, webpage, wallet-frontend

### 2. Creating react-frontend

The App.js file is the entry point for frontend webpage. It defines a number of routes.

The Routes are enclosed within Switch which is inturn enclosed within BrowserRouter tag. 
1. The BrowserRouter tag is required for defining routes.
2. The Switch tag is used to match the first url pattern, but if you look at it, it can be removed (To-Do)
3. The Redirect tag is used to redirect to another route

In App.js we have included getWeb3.js, which creates and returns a Web3 instance depending on the provider. The getWeb3.js file was written by me but it can be downloaded by doing "truffle unbox react".

Then in the components folder we create all the components. The main components are HomePage, ProfilePage and TransactionPage. These are the main three views to which App.js routes. These then make use of the Profile, TransactionList, ContactList, SaveContact, SearchBar. TransactionList and ContactList components further make use of ContactCard and TransactionBrief components respectively.

All the components recieve web3 instance as a prop. This was passed at the top by App.js as is evident from 
```python
component={(props)=><ProfilePage web3 = {this.state.web3} {...props}>}
```

"The {...props} was included in every component so that they can access the matched url using this.props.params.matched"

### 3. Creating the django backend

The backend consists of two apps webpage and api.
1. api is used for handling api calls
2. webpage is used for serving the react page

#### 3.1. api app (/api/)

To enable cors we used django-cors-header package.In settings.py file 
1. add 'corsheaders' to INSTALLED_APPS
2. add 'corsheaders.middleware.CorsMiddleware' & 'django.middleware.common.CommonMiddleware' to MIDDLEWARE
3. add CORS_ORIGIN_ALLOW_ALL = True, you may also supply a list of allowed origins by assigning it to CORS_ORIGIN_WHITELIST but CORS_ORIGIN_ALLOW_ALL superceeds it.

#### 3.2. webpage app (/index/)

This app is used to serve the react frontend.

First build the complete react app as 
```
npm run build
```

The output files will be available in the build folder of the frontend project. We need to add te path of this folder in our settings.py file so that it can find the recources to serve. For that, in the settings.py file -
1. add 'DIRS' : [os.path.join(BASE_DIR, 'wallet-frontend')] to TEMPLATES # since the frontnd project is located inside the wallet-frontend folder inside the root directory of django project
2. add STATICFILE_DIRS = ( 
    os.path.join(BASE_DIR, 'wallet-frontend', 'build', 'static')
)

In webpage.views.py in the method that will render the react app return *render(request, 'build/index.html')* where render can be imported from django.shortcuts

