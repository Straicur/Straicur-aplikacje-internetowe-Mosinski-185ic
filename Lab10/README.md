# Lab 10 Django + React (aplikacja typu ToDo)


## Wygląd strony:
W poniższych screanach pokazana jest funkcjonalność oraz dane po stronie Frontend jak i Backend .
![list](/Lab10/SCR//3.PNG "Start")

![list](/Lab10/SCR//4.PNG "Start")

![list](/Lab10/SCR//5.PNG "Start")

![list](/Lab10/SCR//6.PNG "Start")

![list](/Lab10/SCR//1.PNG "Start")

![list](/Lab10/SCR//2.PNG "Start")

## Backend w Diango z DRF Zmiany

Najpierw instalacja nowych pakietów.
```pip install django-cors-headers ```
```pip install djangorestframework ```
Settings.py
``` python 
INSTALLED_APPS = [
    ...
    'corsheaders',         
    'rest_framework',
    'todo',     
  ]
```

``` python 
 MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',      
    ...
]
```
``` python 
CORS_ORIGIN_WHITELIST = [
     'http://localhost:3000',
     'http://localhost:8000',
]
```
Todo/Models.py 
``` python 
from django.db import models
from django.utils import timezone

class Todo(models.Model):
  title = models.CharField(max_length=120, blank=False, default='')
  description = models.TextField(max_length=200,blank=False, default='')
  completed = models.BooleanField(default=False)
  data_publikacji = models.DateField(blank=True, default=timezone.now)
  
  def _str_(self):
    return self.title 
```
Todo/Serializers.py
``` python 
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = ('id', 'title', 'description', 'completed','data_publikacji')
```
Todo/views.py
``` python 
from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import TodoSerializer     
from .models import Todo        
from rest_framework import generics             

class TodoView(viewsets.ModelViewSet):      
    serializer_class = TodoSerializer          
    queryset = Todo.objects.all()      

class DetailTodo(generics.RetrieveAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    

```

## Frontend React Zmiany
Po stworzeniu apki i zainstalowaniu bootstrapa przechodzimy do zmian .

index.js
``` python 
import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.min.css';       
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import "./App.css";
ReactDOM.render(<App />, document.getElementById('root'));
// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
```
Plik serviceWorker.js który nie był zawarty w poradniku. 
``` python 
// This optional code is used to register a service worker.
// register() is not called by default.

// This lets the app load faster on subsequent visits in production, and gives
// it offline capabilities. However, it also means that developers (and users)
// will only see deployed updates on subsequent visits to a page, after all the
// existing tabs open on the page have been closed, since previously cached
// resources are updated in the background.

// To learn more about the benefits of this model and instructions on how to
// opt-in, read https://bit.ly/CRA-PWA

const isLocalhost = Boolean(
    window.location.hostname === 'localhost' ||
      // [::1] is the IPv6 localhost address.
      window.location.hostname === '[::1]' ||
      // 127.0.0.0/8 are considered localhost for IPv4.
      window.location.hostname.match(
        /^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/
      )
  );
  
  export function register(config) {
    if (process.env.NODE_ENV === 'production' && 'serviceWorker' in navigator) {
      // The URL constructor is available in all browsers that support SW.
      const publicUrl = new URL(process.env.PUBLIC_URL, window.location.href);
      if (publicUrl.origin !== window.location.origin) {
        // Our service worker won't work if PUBLIC_URL is on a different origin
        // from what our page is served on. This might happen if a CDN is used to
        // serve assets; see https://github.com/facebook/create-react-app/issues/2374
        return;
      }
  
      window.addEventListener('load', () => {
        const swUrl = `${process.env.PUBLIC_URL}/service-worker.js`;
  
        if (isLocalhost) {
          // This is running on localhost. Let's check if a service worker still exists or not.
          checkValidServiceWorker(swUrl, config);
  
          // Add some additional logging to localhost, pointing developers to the
          // service worker/PWA documentation.
          navigator.serviceWorker.ready.then(() => {
            console.log(
              'This web app is being served cache-first by a service ' +
                'worker. To learn more, visit https://bit.ly/CRA-PWA'
            );
          });
        } else {
          // Is not localhost. Just register service worker
          registerValidSW(swUrl, config);
        }
      });
    }
  }
  
  function registerValidSW(swUrl, config) {
    navigator.serviceWorker
      .register(swUrl)
      .then(registration => {
        registration.onupdatefound = () => {
          const installingWorker = registration.installing;
          if (installingWorker == null) {
            return;
          }
          installingWorker.onstatechange = () => {
            if (installingWorker.state === 'installed') {
              if (navigator.serviceWorker.controller) {
                // At this point, the updated precached content has been fetched,
                // but the previous service worker will still serve the older
                // content until all client tabs are closed.
                console.log(
                  'New content is available and will be used when all ' +
                    'tabs for this page are closed. See https://bit.ly/CRA-PWA.'
                );
  
                // Execute callback
                if (config && config.onUpdate) {
                  config.onUpdate(registration);
                }
              } else {
                // At this point, everything has been precached.
                // It's the perfect time to display a
                // "Content is cached for offline use." message.
                console.log('Content is cached for offline use.');
  
                // Execute callback
                if (config && config.onSuccess) {
                  config.onSuccess(registration);
                }
              }
            }
          };
        };
      })
      .catch(error => {
        console.error('Error during service worker registration:', error);
      });
  }
  
  function checkValidServiceWorker(swUrl, config) {
    // Check if the service worker can be found. If it can't reload the page.
    fetch(swUrl, {
      headers: { 'Service-Worker': 'script' }
    })
      .then(response => {
        // Ensure service worker exists, and that we really are getting a JS file.
        const contentType = response.headers.get('content-type');
        if (
          response.status === 404 ||
          (contentType != null && contentType.indexOf('javascript') === -1)
        ) {
          // No service worker found. Probably a different app. Reload the page.
          navigator.serviceWorker.ready.then(registration => {
            registration.unregister().then(() => {
              window.location.reload();
            });
          });
        } else {
          // Service worker found. Proceed as normal.
          registerValidSW(swUrl, config);
        }
      })
      .catch(() => {
        console.log(
          'No internet connection found. App is running in offline mode.'
        );
      });
  }
  
  export function unregister() {
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.ready
        .then(registration => {
          registration.unregister();
        })
        .catch(error => {
          console.error(error.message);
        });
    }
  }
```
Modal.js
``` python 
    
    import React, { Component } from "react";
    import DatePicker from 'react-date-picker'
    import {
      Button,
      Modal,
      ModalHeader,
      ModalBody,
      ModalFooter,
      Form,
      FormGroup,
      Input,
      Label
    } from "reactstrap";

    export default class CustomModal extends Component {
      constructor(props) {
        super(props);
        this.state = {
          activeItem: this.props.activeItem
        };
      }
      handleChange = e => {
        let { name, value } = e.target;
        if (e.target.type === "checkbox") {
          value = e.target.checked;
        }
        const activeItem = { ...this.state.activeItem, [name]: value };
        this.setState({ activeItem });
      };
      render() {
        const { toggle, onSave } = this.props;
        return (
          <Modal isOpen={true} toggle={toggle}>
            <ModalHeader toggle={toggle}> Todo Item </ModalHeader>
            <ModalBody>
              <Form>
                <FormGroup>
                  <Label for="title">Tytuł</Label>
                  <Input
                    type="text"
                    name="title"
                    value={this.state.activeItem.title}
                    onChange={this.handleChange}
                    placeholder="Enter Todo Title"
                  />
                </FormGroup>
                <FormGroup>
                  <Label for="description">Opis</Label>
                  <Input
                    type="text"
                    name="description"
                    value={this.state.activeItem.description}
                    onChange={this.handleChange}
                    placeholder="Enter Todo description"
                  />
                </FormGroup>
                <FormGroup check>
                  <Label for="completed">
                    <Input
                      type="checkbox"
                      name="completed"
                      checked={this.state.activeItem.completed}
                      onChange={this.handleChange}
                    />
                    Skończone
                  </Label>
                </FormGroup>
              </Form>
            </ModalBody>
            <ModalFooter>
              <Button color="success" onClick={() => onSave(this.state.activeItem)}>
                Zapisz
                
              </Button>
            </ModalFooter>
          </Modal>
        );
      }
    }

```
App.js
``` python 

    import React, { Component } from "react";
    import Modal from "./components/Modal";
    import axios from "axios";

    class App extends Component {
      constructor(props) {
        super(props);
        this.state = {
          viewCompleted: false,
          activeItem: {
            title: "",
            description: "",
            completed: false
          },
          todoList: []
        };
      }
      componentDidMount() {
        this.refreshList();
      }
      refreshList = () => {
        axios
          .get("/api/todos/")
          .then(res => this.setState({ todoList: res.data }))
          .catch(err => console.log(err));
      };
      displayCompleted = status => {
        if (status) {
          return this.setState({ viewCompleted: true });
        }
        return this.setState({ viewCompleted: false });
      };
      renderTabList = () => {
        return (
          <div className="my-5 tab-list">
            <span
              onClick={() => this.displayCompleted(true)}
              className={this.state.viewCompleted ? "active" : ""}
            >
              Skończone
            </span>
            <span
              onClick={() => this.displayCompleted(false)}
              className={this.state.viewCompleted ? "" : "active"}
            >
              Nieskończone
            </span>
          </div>
        );
      };
      renderItems = () => {
        const { viewCompleted } = this.state;
        const newItems = this.state.todoList.filter(
          item => item.completed === viewCompleted
        );
        return newItems.map(item => (
          <li
            key={item.id}
            className="list-group-item d-flex justify-content-between align-items-center"
          >
            <span
              className={`todo-title mr-2 ${
                this.state.viewCompleted ? "completed-todo" : ""
              }`}
              title={item.description}
            >
              {" Tytuł:  "}
              {item.title}
              {" | "}
              {" Opis:  "}
              {item.description}
              {" | "}
              {"  Stworzone :"}
              {"  "}
              {item.data_publikacji}
            </span>
            <span>
              <button
                onClick={() => this.editItem(item)}
                className="btn btn-dark mr-2"
              >
                {" "}
                Edytuj{" "}
              </button>
              <button
                onClick={() => this.handleDelete(item)}
                className="btn btn-danger"
              >
                Usuń{" "}
              </button>
            </span>
          </li>
        ));
      };
      toggle = () => {
        this.setState({ modal: !this.state.modal });
      };
      handleSubmit = item => {
        this.toggle();
        if (item.id) {
          axios
            .put(`http://localhost:8000/api/todos/${item.id}/`, item)
            .then(res => this.refreshList());
          return;
        }
        axios
          .post("http://localhost:8000/api/todos/", item)
          .then(res => this.refreshList());
      };
      handleDelete = item => {
        axios
          .delete(`http://localhost:8000/api/todos/${item.id}/`)
          .then(res => this.refreshList());
      };
     
      createItem = () => {
        const item = { title: "", description: "", completed: false };
        this.setState({ activeItem: item, modal: !this.state.modal });
      };
      editItem = item => {
        this.setState({ activeItem: item, modal: !this.state.modal });
      };
      render() {
        return (
          <main className="content">
            <h1 className="text-white text-uppercase text-center my-4">Todo</h1>
            <div className="row ">
              <div className="col-md-6 col-sm-10 mx-auto p-0">
                <div className="card p-3 szer">
                  <div className="">
                    <button onClick={this.createItem} className="btn btn-primary">
                      Dodaj zadanie
                    </button>
                  </div>
                  {this.renderTabList()}
                  <ul className="list-group list-group-flush">
                    {this.renderItems()}
                  </ul>
                </div>
              </div>
            </div>
            {this.state.modal ? (
              <Modal
                activeItem={this.state.activeItem}
                toggle={this.toggle}
                onSave={this.handleSubmit}
              />
            ) : null}
          </main>
        );
      }
    }
    export default App;
```

## Zmiany 

Dodałem do modelu created_at , w frontendzie kilka poprawek oraz wyświetlam Tytuł , Opis oraz Date stworzenia zamias samego tytułu .
Co do błędu ``` Access to XMLHttpRequest at 'http://localhost:8000/api/todos/' from origin 'http://localhost:3000' has been blocked by CORS policy: Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present on the requested resource. ```
Spotkałem się z nim w google chromie (wystarczy dodać rozszerzenie) .
