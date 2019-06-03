// //// the code for calculator wont work. to make it work, copy the return part fom Calculator.js and paste it where we have called <Calculator />
//
// import React, {Component} from "react";
// import ReactDOM from 'react-dom';
// import {BrowserRouter as Router, Route, Redirect} from "react-router-dom";
// import DummyPage from './dummyPage';
// import AppRouter from './router';
// class App extends Component {
//     state = { value: 0,
//              array: [1,2,3,4,5],
//              userChoice: 0,
//              firstNumber: 0,
//              secondNumber: 0,
//              finalResult: 0,
//              button1: 1,
//              button2: 2,
//              button3: 3,
//              button4: 4,
//              button5: 5,
//              button6: 6,
//              button7: 7,
//              button8: 8,
//              button9: 9,
//              user1: true,
//              user2: false,
//              todoList: [ ],
//              currentTodo: "",
//              todoItemToBeUpdated: "",
//              updatedTodoValue: "",
//              userName: "",
//              password: "",
//              registeredUsers: [],
//              userToBeDeleted: ""
//             }
//
//     renderCurrentUserArea() {
//
//         if (this.state.user1 == true) {
//             return (
//                 <div>
//                     <br />
//                     Its your turn user1
//                  </div>
//             )
//         } else if (this.state.user2 == true) {
//             return (
//                  <div>
//                     <br />
//                     Its your turn user2
//                  </div>
//             )
//         }
//     }
//
//     componentDidMount() {
//       this.makeRequest()
//     }
//
//     navigateToPage = event => {
//       return <AppRouter />
//     }
//
//
//     handleUserName = event => {
//         this.setState({userName: event.target.value});
//     }
//
//     handlePassword = event => {
//         this.setState({password: event.target.value})
//     }
//
//     handleUserToBeDeleted = event => {
//       this.setState({userToBeDeleted: event.target.value});
//     }
//
//     makeDeleteRequest = event => {
//       let localhostUrl = 'http://localhost:5454/posts/'
//       let userToBeDeleted = this.state.userToBeDeleted.toString()
//       let filteredUser = this.state.registeredUsers.filter(function(userObject){
//          return userObject.title == userToBeDeleted
//       })
//       let filteredUserObjectId = filteredUser[0].id.toString()
//
//       let completeUrl = localhostUrl + filteredUserObjectId
//       fetch(completeUrl, {
//         method: 'DELETE',
//         headers: {
//           'Content-Type': 'application/json'
//         }
//       })
//     }
//
//     submitForm = event => {
//       let jsonDummyData = JSON.stringify({
//         title: this.state.userName,
//         tags: this.state.password
//       })
//
//       fetch('http://localhost:5454/posts', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json'
//         },
//         body: jsonDummyData
//       })
//       .then(res => res.json())
//     }
//
//     renderWinnerArea() {
//           if ((this.state.button1 == "X" && this.state.button2 == "X" && this.state.button3 == "X")) {
//             return (
//                 <p> The winner is user1 </p>
//             )
//         } else if ((this.state.button1 == "O" && this.state.button2 == "O" && this.state.button3 == "O")) {
//             return (
//                 <p> The winner is user2 </p>
//             )
//         } else if (this.state.button1 == "X" && this.state.button4 == "X" && this.state.button7 == "X") {
//             return (
//                 <p> The winner is user1 </p>
//             )
//         } else if (this.state.button1 == "O" && this.state.button4 == "O" && this.state.button7 == "O") {
//             return (
//                 <p> The Winner is user2 </p>
//             )
//         } else if (this.state.button4 == "X" && this.state.button5 == "X" && this.state.button6 == "X") {
//             return (
//                 <p> The winner is user1 </p>
//             )
//         } else if (this.state.button7 == "X" && this.state.button8 == "X" && this.state.button9 == "X") {
//             return (
//                 <p> The winner is user1 </p>
//             )
//         } else if (this.state.button4 == "O" && this.state.button5 == "O" && this.state.button6 == "O") {
//             return (
//                 <p> The winner is user2 </p>
//             )
//         } else if (this.state.button7 == "O" && this.state.button8 == "O" && this.state.button9 == "O") {
//             return (
//                 <p> The winner is user2 </p>
//             )
//         } else if (this.state.button2 == "X" && this.state.button5 == "X" && this.state.button8 == "X") {
//             return (
//                 <p> The winner is user1 </p>
//             )
//         } else if (this.state.button3 == "X" && this.state.button6 == "X" && this.state.button9 == "X") {
//             return (
//                 <p> The winner is user1 </p>
//             )
//         } else if (this.state.button2 == "O" && this.state.button5 == "O" && this.state.button8 == "O") {
//             return (
//                 <p> the winner is user2 </p>
//             )
//         } else if (this.state.button3 == "O" && this.state.button6 == "O" && this.state.button9 == "O") {
//             return (
//                 <p> The winner is user2 </p>
//             )
//         } else if (this.state.button1 == "X" && this.state.button5 == "X" && this.button9 == "X") {
//             return (
//                 <p> The winner is user1 </p>
//             )
//         } else if (this.state.button3 == "X" && this.state.button5 == "X" && this.state.button7 == "X") {
//             return (
//                 <p> The winner is user1 </p>
//             )
//         } else if (this.state.button1 == "O" && this.state.button5 == "O" && this.button9 == "O") {
//             return (
//                 <p> the winner is user2 </p>
//             )
//         } else if (this.state.button3 == "O" && this.state.button5 == "O" && this.state.button7 == "O") {
//             return (
//                 <p> the winner is user2 </p>
//             )
//         }
//     }
//     handleButton1Change = event => {
//         if (this.state.user1 == true) {
//          this.setState({button1: "X", user1: false, user2: true});
//         } else if (this.state.user2 == true) {
//
//             this.setState({button1: "O", user1: true, user2: false});
//         }
//     }
//
//     handleButton2Change = event => {
//         if (this.state.user1 == true) {
//             this.setState({button2: "X", user1: false, user2: true})
//         } else if (this.state.user2 == true) {
//             this.setState({button2: "O", user1: true, user2: false});
//         }
//     }
//
//     handleButton3Change = event => {
//         if (this.state.user1 == true) {
//             this.setState({button3: "X", user1: false, user2: true})
//         } else if (this.state.user2 == true) {
//             this.setState({button3: "O", user1: true, user2: false});
//         }
//     }
//
//     handleButton4Change = event => {
//         if (this.state.user1 == true) {
//             this.setState({button4: "X", user1: false, user2: true})
//         } else if (this.state.user2 == true) {
//             this.setState({button4: "O", user1: true, user2: false});
//         }
//     }
//
//     handleButton5Change = event => {
//         if (this.state.user1 == true) {
//             this.setState({button5: "X", user1: false, user2: true})
//         } else if (this.state.user2 == true) {
//             this.setState({button5: "O", user1: true, user2: false});
//         }
//     }
//
//     handleButton6Change = event => {
//         if (this.state.user1 == true) {
//             this.setState({button6: "X", user1: false, user2: true})
//         } else if (this.state.user2 == true) {
//             this.setState({button6: "O", user1: true, user2: false});
//         }
//     }
//
//     handleButton7Change = event => {
//         if (this.state.user1 == true) {
//             this.setState({button7: "X", user1: false, user2: true})
//         } else if (this.state.user2 == true) {
//             this.setState({button7: "O", user1: true, user2: false});
//         }
//     }
//
//     handleButton8Change = event => {
//         if (this.state.user1 == true) {
//             this.setState({button8: "X", user1: false, user2: true})
//         } else if (this.state.user2 == true) {
//             this.setState({button8: "O", user1: true, user2: false});
//         }
//     }
//
//     handleButton9Change = event => {
//         if (this.state.user1 == true) {
//             this.setState({button9: "X", user1: false, user2: true})
//         } else if (this.state.user2 == true) {
//             this.setState({button9: "O", user1: true, user2: false});
//         }
//     }
//
//     handleChange = event => {
//         this.setState({value: event.target.value});
//     }
//
//     performAddition = event => {
//         let updatedFinalResult = Number(this.state.firstNumber) + Number(this.state.secondNumber )
//         this.setState({finalResult: updatedFinalResult});
//     }
//
//     performSubtraction = event => {
//         let firstNumber = Number(this.state.firstNumber)
//         let secondNumber = Number(this.state.secondNumber)
//         if (firstNumber > secondNumber) {
//             this.setState({finalResult: (firstNumber - secondNumber)});
//         } else {
//             this.setState({finalResult: (secondNumber - firstNumber)});
//         }
//
//     }
//
//     performDivision = event => {
//         let firstNumber = Number(this.state.firstNumber)
//         let secondNumber = Number(this.state.secondNumber)
//
//         if (firstNumber > secondNumber) {
//             this.setState({finalResult: (firstNumber / secondNumber)});
//         } else {
//             this.setState({finalResult: (secondNumber / firstNumber)});
//         }
//     }
//
//     performMultiplication = event => {
//         this.setState({finalResult: (Number(this.state.firstNumber) * Number(this.state.secondNumber))});
//     }
//
//     addValue = event => {
//         let incrementedValue = Number(this.state.value + 1)
//         this.setState({value:  incrementedValue});
//     }
//
//     subtractValue = event => {
//         let decrementedValue = Number(this.state.value - 1)
//         this.setState({value: decrementedValue});
//     }
//
//     handleUserChoice1 = event => {
//         this.setState({userChoice: 1});
//     }
//
//     handleUserChoice2 = event => {
//         this.setState({userChoice: 2});
//     }
//
//     handleChangeForFirstNumber = event => {
//         this.setState({firstNumber: event.target.value});
//     }
//
//     handleChangeForSecondNumber = event => {
//         this.setState({secondNumber: event.target.value});
//     }
//
//     renderTicTacToe = event => {
//         this.setState({userChoice: 4});
//     }
//
//     renderTodo = event => {
//         this.setState({userChoice: 5});
//     }
//
//     renderForm = event => {
//         this.setState({userChoice: 6});
//     }
//
//     renderDeleteRequestArea = event => {
//       this.setState({userChoice: 7})
//     }
//
//     modifyArray = event => {
//         const arr = this.state.array
//         const updatedArray = arr.map((arrayValue) =>
//             <li> {arrayValue * 2} </li>
//         );
//         return updatedArray
//
//     }
//
//     refreshScreen = event => {
//         this.setState({userChoice: -10});
//     }
//
//     renderCalculator = event => {
//         this.setState({userChoice: 3});
//     }
//
//     handleCurrentTodo = event => {
//         this.setState({currentTodo: event.target.value});
//     }
//
//
//
//     addTodo = event => {
//         let todoList = this.state.todoList
//         let currentTodo = this.state.currentTodo
//         this.setState({todoList: todoList.concat([currentTodo])})
//     }
//
//     deleteTodo = (todoItem) => {
//         let todoList = this.state.todoList
//         this.setState({todoList: (todoList.filter(function(todo){
//             return todo != todoItem
//         }))})
//     }
//
//
//     renderEditableTodoComponent = (todoItem) => {
//         let todoList = this.state.todoList
//         todoList.map((todo) =>
//             (todo != todoItem) ? <p> True </p> : <p> False </p>
//             ) }
//
//     updateTodoItem = (todo) => {
//         this.setState({todoItemToBeUpdated: todo})
//     }
//
//     renderEditableTodo = (todo) => {
//         let todoItem  = this.state.todoItemToBeUpdated
//         return ( todoItem != todo ? this.renderEditableTodoComponent(todo) : <div> </div>
//         )
//     }
//
//     renderAddedTodosArea = event => {
//         return this.state.todoList.map((todo) =>
//                 <div>
//                <li> {todo} {" "}
//                 {" "}
//                 <input type = "button" value = "Delete Todo" onClick = {() => this.deleteTodo({todo})} />
//                 {" "}
//                 <input type = "button" value = "Edit Todo" onClick = {() => this.updateTodoItem({todo})} />
//
//                 {" "}
//                 {this.renderEditableTodo(todo)}
//                 </li>
//                 <br />
//                 </div>
//         );
//
//     }
//
//     makeRequest = event => {
//        let registeredUsers = this.state.registeredUsers
//
//         fetch('http://localhost:5454/posts'
//         )
//         .then(resp => resp.json())
//         .then(data => this.setState({registeredUsers: data}))
//
//     }
//
//     handleNavigationChoice = event => {
//       this.setState({userChoice: 8})
//     }
//
//     renderhtmlForUserChoice(){
//         if (this.state.userChoice == 1) {
//             return (
//                 <div>
//             <br />
//             <input type="button"
//              value= "+"
//               onClick = {this.addValue} />
//             {" "}
//             <input
//              type="text"
//              value = {this.state.value}
//              onChange = {this.handleChange} />
//             {" "}
//             <input type="button"
//              value=  "-"//{this.state.value}
//              onClick = {this.subtractValue} />
//
//             </div>
//             )
//
//         } else if (this.state.userChoice == 2) {
//             return (
//                 <div>
//                  initial Array: <br /> [1,2,3,4,5]
//                   <br />
//                  doubled Array :
//                      <div>
//                         {this.modifyArray()}
//                      </div>
//                 </div>
//             )
//
//         } else if (this.state.userChoice == -10 || this.state.userChoice > 8) {
//             return (<p> </p>)
//
//         } else if (this.state.userChoice == 3) {
//                 return (
//                     <div>
//                     <input
//                         type = "text"
//                         value = {this.state.firstNumber}
//                         onChange = {this.handleChangeForFirstNumber} />
//                     <br />
//                     <input
//                         type = "text"
//                         value = {this.state.secondNumber}
//                         onChange = {this.handleChangeForSecondNumber} />
//                     <br />
//                     <input
//                         readOnly
//                         value = {this.state.finalResult}
//                         />
//                     < br />
//                      <input
//                         type = "button"
//                         value = "+"
//                         onClick = {this.performAddition} />
//                     {" "}
//                      <input
//                         type = "button"
//                         value = "-"
//                         onClick = {this.performSubtraction} />
//                     {" "}
//                       <input
//                         type = "button"
//                         value = "/"
//                         onClick = {this.performDivision} />
//                     {" "}
//                       <input
//                         type = "button"
//                         value = "*"
//                         onClick = {this.performMultiplication} />
//                  </div>
//                 )
//         } else if (this.state.userChoice == 4) {
//             return (
//               <div>
//                 <div>
//                  <input
//                     type = "button"
//                     value = {this.state.button1}
//                     onClick = {this.handleButton1Change} />
//                 <input
//                     type = "button"
//                     value = {this.state.button2}
//                     onClick = {this.handleButton2Change} />
//                 <input
//                     type = "button"
//                     value = {this.state.button3}
//                     onClick = {this.handleButton3Change} />
//                 <br />
//                  <input
//                     type = "button"
//                     value = {this.state.button4}
//                     onClick = {this.handleButton4Change} />
//                 <input
//                     type = "button"
//                     value = {this.state.button5}
//                     onClick = {this.handleButton5Change} />
//                 <input
//                     type = "button"
//                     value = {this.state.button6}
//                     onClick = {this.handleButton6Change} />
//                 <br />
//                 <input
//                     type = "button"
//                     value = {this.state.button7}
//                     onClick = {this.handleButton7Change} />
//
//                 <input
//                     type = "button"
//                     value = {this.state.button8}
//                     onClick = {this.handleButton8Change} />
//
//                 <input
//                     type = "button"
//                     value = {this.state.button9}
//                     onClick = {this.handleButton9Change} />
//
//                 <div>
//                   {this.renderCurrentUserArea()}
//                 </div>
//
//                 <div>
//                     {this.renderWinnerArea()}
//                 </div>
//
//                 </div>
//                 </div>
//             )
//         } else if (this.state.userChoice == 5) {
//             return (
//                 <div>
//                     <input
//                         type = "text"
//                         value = {this.state.currentTodo}
//                         onChange = {this.handleCurrentTodo} />
//                     {" "}
//                     <input
//                         type = "button"
//                         value = "Add Todo"
//                         onClick = {this.addTodo} />
//                      {" "}
//                     <br />
//                     <p> TODO'S </p>
//                     <br />
//
//                     <div>
//                         {this.renderAddedTodosArea()}
//                     </div>
//                 </div>
//             )
//         } else if (this.state.userChoice == 6) {
//             return (
//                 <div>
//                     <input type = "text" value= {this.state.userName} onChange = {this.handleUserName}/>
//                     <br />
//                     <input type = "text" value = {this.state.password} onChange ={this.handlePassword} />
//                     <br />
//                     <input type = "button" value = "Submit" onClick = {this.submitForm} />
//                 </div>
//             )
//         } else if (this.state.userChoice == 7) {
//           return (
//             <div>
//              <br />
//              {" "}
//               <input type = "text" value = {this.state.userToBeDeleted} onChange = {this.handleUserToBeDeleted} />
//               {" "}
//               <br />
//               <input type = "button" value = "Delete" onClick = {this.makeDeleteRequest} />
//              </div>
//
//           )
//         } else if (this.state.userChoice == 8) {
//           return (
//             <div>
//                 {this.navigateToPage()}
//             </div>
//           )
//         }
//     }
//     render() {
//         return (
//             <div>
//
//             <div>
//              Click on the button of your choice. Enjoy! : ) <br />
//
//             <input
//               type = "button"
//               value = "+ - game "
//               onClick = {this.handleUserChoice1} />
//             {" "}
//              <input
//                type= "button"
//                value= "array updation"
//                onClick = {this.handleUserChoice2} />
//             {" "}
//                 <input
//                     type = "button"
//                     value = "Open Calculator"
//                     onClick = {this.renderCalculator} />
//             {" "}
//               <input
//                 type = "button"
//                 value = "Tic Tac Toe"
//                 onClick = {this.renderTicTacToe} />
//             {" "}
//                 <input
//                  type = "button"
//                  value = "Todo"
//                  onClick = {this.renderTodo} />
//             {" "}
//                 <input
//                  type = "button"
//                  value = "Make GET request"
//                  onClick = {this.makeRequest} />
//             {" "}
//                 <input
//                  type = "button"
//                  value = "Open Form"
//                  onClick = {this.renderForm} />
//             {" "}
//                 <input
//                   type = "button"
//                   value = "Navigate"
//                   onClick = {this.handleNavigationChoice} />
//             {" "}
//              <input
//                 type = "button"
//                 value = "Refresh screen"
//                 onClick = {this.refreshScreen} />
//
//             {" "}
//               <input
//                 type = "button"
//                 value = "Make Delete Request"
//                 onClick = {this.renderDeleteRequestArea} />
//             </div>
//
//             <div>
//              {this.renderhtmlForUserChoice()}
//             </div>
//
//             </div>
//
//         )
//     }
// }
// ReactDOM.render(<App />,document.getElementById('root'));
// export default App;
// <Link to="/home_page"> Dummy Text </Link>
//
// import React from 'react'
// import LoginRouter from './router'
// import HomePage from './router'
//
// class App extends React.Component {
//   constructor(props) {
//     super(props);
//   }
//   state = {
//     userInfo: "dummy Name"
//   }
//   render () {
//     return (
//       <div>
//
//       <HomePage userInformation ={this.state.userInfo}/>
//     </div>
//
//   )
//   }
// }
// export default App



// import React, { Component } from 'react';
// // import reactLogo from './logo-react.svg';
// // import djangoLogo from './logo-django.svg';
// import {BrowserRouter as Router, Route, Redirect} from "react-router-dom";
// import Homepage from './router'
// import './App.css';
// import Button from 'react-bootstrap/Button';
// import ButtonToolbar from 'react-bootstrap/ButtonToolbar';
// // import LoginComponent from './login';
//
// class App extends Component {
//     constructor(props) {
//         super(props);
//     }
//     state = {
//         content: "main page",
//         userName: "",
//         password: "",
//         emailId: "",
//         phoneNumber: "",
//         userObject: {username: "", password: "", emailId: "", phoneNumber: ""}
//     }
//
//
//   renderRegisterForm = event => {
//       {this.setState({content: "register form"})}
//   }
//
//   renderLoginPage = event => {
//       {this.setState({content: "login page"})}
//   }
//
//   updateStateUsername = event => {
//       {this.setState({userName: event.target.value})}
//   }
//
//   updateUserEmailId = event => {
//       {this.setState({emailId: event.target.value})}
//   }
//
//   updatePhoneNumber = event => {
//       {this.setState({phoneNumber: event.target.value})}
//   }
//
//   updateStatePassword = event => {
//       {this.setState({password: event.target.value})}
//   }
//
//
//
//   InitializeUserObject(response) {
//       let userObject = Object.assign({}, this.state.userObject)
//       userObject.username = response.username
//       userObject.password = response.password
//       userObject.emailId = response.emailId
//       userObject.phoneNumber = response.phoneNumber
//       this.setState({userObject})
//       this.setState({content: "Home-Page"})
//   }
//
//   loginUser = event => {
//       let userName = this.state.userName
//       let password = this.state.password
//       console.log(this.state.content, "+++++++++++++++++++++")
//
//       let userLoginDetailsObject =
//            JSON.stringify({
//                username: userName,
//                password: password
//            })
//
//       try {
//           fetch('http://127.0.0.1:8000/login_user/',{
//               method: 'POST',
//               headers: {
//                   'Content-Type': 'application/json'
//               },
//               body: userLoginDetailsObject
//           })
//           .then(response => response.json())
//           .then(resp => this.InitializeUserObject(resp) )
//       }
//       catch(err) {
//           console.log(err, "Error")
//       }
//   }
//
//   registerUser = event => {
//       let userName = this.state.userName
//       let password = this.state.password
//       let emailId = this.state.emailId
//       let phoneNumber = this.state.phoneNumber
//
//       let userDetailsObject = JSON.stringify({
//           username: userName,
//           password: password,
//           emailId: emailId,
//           phoneNumber: phoneNumber
//       })
//
//       try {
//           fetch('http://127.0.0.1:8000/register_user/', {
//               method: 'POST',
//               headers: {
//                    'Content-Type': 'application/json'
//               },
//               body: userDetailsObject
//           })
//           .then(res => console.log(res))
//           .then(data => this.setState({content: "main page"}))
//       }
//       catch(err) {
//           console.log(err, "Error ")
//       }
//   }
//
//   loginForm() {
//
//       return (
//         <div>
//           Enter Username and Password to login
//           <br />
//           Username:
//           {" "}
//           <input type="text" value= {this.state.userName} onChange = {this.updateStateUsername} />
//           <br />
//           Password:
//           {" "}
//           <input type="text" value = {this.state.password} onChange = {this.updateStatePassword} />
//           <br />
//            {" "}
//           <input type="button" value ="Login" onClick = {this.loginUser} />
//           </div>
//       )
//   }
//
//   renderUserHomepage() {
//       return (
//         <div>
//           Welcome Back {this.state.userObject.username}!
//           {" "}
//           {" "}
//           </div>
//
//       )
//   }
//
//   registerForm() {
//
//       return (
//         <div>
//           UserName:
//           {" "}
//
//           <input type="text" value = {this.state.userName} onChange = {this.updateStateUsername} />
//           <br />
//           Password:
//           {" "}
//           <input type="text" value = {this.state.password} onChange = {this.updateStatePassword} />
//           <br />
//           Email:
//           {" "}
//           <input type="text" value= {this.state.emailId} onChange = {this.updateUserEmailId} />
//           <br />
//           Phone Number:
//           {" "}
//           <input type="text" value = {this.state.phoneNumber} onChange = {this.updatePhoneNumber} />
//           <br />
//           <br />
//           <input type = "button" value = "Submit" onClick = {this.registerUser} />
//            </div>
//       )
//   }
//
//   renderMainPage() {
//     return (
//                 <div>
//                 <ButtonToolbar>
//                     <Button variant="danger" class="align-baseline"> Register </Button>
//                 </ButtonToolbar>
//                     {" "}
//                     <input type = "button" value = "Login" onClick = {this.renderLoginPage} />
//                 </div>
//             )
//   }
//
//     render() {
//         if (this.state.content == "main page") {
//             return (
//                 <div>
//                     {this.renderMainPage()}
//                 </div>
//             )
//         } else if (this.state.content == "register form") {
//                 return (
//                     <div>
//                         {this.registerForm()}
//                     </div>
//                 )
//             } else if (this.state.content == "login page") {
//                 return (
//                     <div>
//
//                     </div>
//                 )
//             }else if (this.state.content == "Home-Page"){
//                 return (<Homepage username = {this.state.userName} />)
//             }
//             else {
//                 return (
//                     <div>
//                     Main Page
//                      </div>
//                 )
//             }
//     }
// }
//
// export default App;

import React from 'react'
// import LoginRouter from './router'
// import HomePage from './router'
import Button from 'react-bootstrap/Button';
import ButtonToolbar from 'react-bootstrap/ButtonToolbar';

class App extends React.Component {
  constructor(props) {
    super(props);
  }

  state = {
    isEditorVisible: false,
    typesOfJoins: [
      "(INNER) JOIN: Returns records that have matching values in both tables",
      "LEFT (OUTER) JOIN: Returns all records from the left table and the matched records from the right table",
      "RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table",
      "FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table"
    ],
    expectedAnswer1: "ON Orders.CustomerID",
    expectedAnswer2: "Customers.CustomerID",
    answer1Input: "",
    answer2Input: "",
  }

changeEditorState = event => {
  let isEditorVisible = this.state.isEditorVisible
  this.setState({
    isEditorVisible: ! (isEditorVisible)
  })
}
renderJoinTypesImageArea() {
  let innerJoinImage = require('C:/practiceReactApp/practice_app/src/innerJoin.gif')
  let leftJoinImage = require('C:/practiceReactApp/practice_app/src/leftJoin.gif')
  let rightJoinImage = require('C:/practiceReactApp/practice_app/src/rightJoin.gif')
  let fullOuterJoinImage = require('C:/practiceReactApp/practice_app/src/fullOuterJoin.gif')
  return (
    <div>
      <img src={innerJoinImage} />
      {" "}
      {" "}
      <img src={leftJoinImage} />
      {" "}
      {" "}
      <img src={rightJoinImage} />
      {" "}
      {" "}
      <img src={fullOuterJoinImage} />
    </div>
  )
}

renderQuestionInExerciseArea() {
  return (
    <div>
      <p>
        SELECT *
      </p>
     <p>
        FROM Orders
     </p>
     <p>
        LEFT JOIN Customers
     </p>
     <input type="text"/>
     =
     <input type="text"/>
     ;
    </div>
  )
}

navigateToSubmitAnswerPage() {
  return (
    <div>
      
    </div>
  )
}

renderExerciseArea() {
  return (
    <div class="shadow-none p-4 mb-4 bg-dark">
      <h3 class="text-light"> Test Yourself With Exercises </h3>
      <div class="shadow-sm p-4 mb-4 bg-white">
        <h4> Exercise: </h4>
        <h5>
            Insert the missing parts in the JOIN clause to join the two tables Orders and Customers, using the CustomerID field in both tables as the relationship between the two tables.
        </h5>
        <div class="shadow-none p-4 mb-4 bg-light">
          {this.renderQuestionInExerciseArea()}
         </div>
       </div>
       <Button variant="success" class="align-baseline" onClick = {this.navigateToSubmitAnswerPage}> Submit Answer </Button>
     </div>
  )
}

renderTypesOfJoinArea() {
  return (
    <div>
    {this.state.typesOfJoins.map(joinType => (
      <ul>
        <li type="square"> {joinType}
        </li>
      </ul>
    ))}
    </div>
  )
}

renderEditor () {
  return(
    <div>
      <div class="form-group">
        <label for="comment">:</label>
        <textarea class="form-control" rows="5" id="comment"></textarea>
      </div>
    </div>
  )
}

renderMainPageContent() {
  return(
  <div>
  <h2 class="text-left"> SQL Joins </h2>
  <ButtonToolbar>
    <Button variant="success" class="align-baseline"> Previous </Button>
    <div class="text-center">
    <Button variant="success" class="align-baseline" > Next </Button>
    </div>
   </ButtonToolbar>

  <h4> SQL Join </h4>
  <h5> A JOIN clause is used to combine rows from two or more tables, based on a related column between them. </h5>
  <h5> Let's look at a selection from the "Orders" table: </h5>
  <div>
    {this.renderExampleOrdersTable()}
   </div>
  <h5> Then, look at a selection from the "Customers" table: </h5>
  <br/>
  <div>
  {this.renderExampleCustomersTable()}
  </div>
  <h5>
    Notice that the "CustomerID" column in the "Orders" table refers to the "CustomerID" in the "Customers" table.The relationship between the two tables above is the "CustomerID" column.
  </h5>
  <br/>
  <h5>
    Then,we can create the following SQL statement (that contains an INNER JOIN), that selects records that have matching values in both tables:
  </h5>
  {this.renderExampleArea()}
  <h5>
    and it will produce something like this:
  </h5>
  <div>
      {this.renderOutputJoinedTable()}
   </div>
  <h2 class="text-left"> Different Types of SQL JOINs </h2>
  <h5> Here are the different types of the JOINs in SQL: </h5>
 <div>
    {this.renderTypesOfJoinArea()}
  </div>
<div>
  {this.renderJoinTypesImageArea()}
 </div>
 <br/>
 <div>
  {this.renderExerciseArea()}
 </div>
</div>
)
}


renderExampleArea() {
  return (
    <div class="shadow-none p-4 mb-4 bg-light">
    <h4> Example </h4>
      <div class="shadow-sm p-4 mb-4 bg-white">
              <p> SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
              </p>
              <p> FROM Orders
              </p>
              <p> INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;
              </p>
      </div>
      <Button variant="success" class="align-baseline" onClick = {this.changeEditorState}> Try it Yourself >> </Button>
    </div>
  )
}

renderOutputJoinedTable() {
  return(
    <div>
    <table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">OrderID</th>
      <th scope="col">CustomerName</th>
      <th scope="col">OrderDate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">10308</th>
      <td>Ana Trujillo Emparedados y helados</td>
      <td>9/18/1996</td>
    </tr>
    <tr>
      <th scope="row">10365</th>
      <td>Antonio Moreno Taquería</td>
      <td>11/27/1996</td>
    </tr>
    <tr>
      <th scope="row">10383</th>
      <td>Around the Horn</td>
      <td>12/16/1996</td>
    </tr>
    <tr>
      <th scope="row">10355</th>
      <td>Around the Horn</td>
      <td>11/15/1996</td>
    </tr>
    <tr>
      <th scope="row">10278</th>
      <td>Berglunds snabbköp</td>
      <td>12/16/1996</td>
    </tr>
  </tbody>
</table>
     </div>
  )
}

renderExampleOrdersTable() {
  return (
    <div>
    <table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">OrderID</th>
      <th scope="col">CustomerID</th>
      <th scope="col">OrderDate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">10308</th>
      <td>2</td>
      <td>1996-09-18</td>
    </tr>
    <tr>
      <th scope="row">10309</th>
      <td>37</td>
      <td>1996-09-19</td>
    </tr>
    <tr>
      <th scope="row">10310</th>
      <td>77</td>
      <td>1996-09-20</td>
    </tr>
  </tbody>
</table>
     </div>
  )
}


renderExampleCustomersTable() {
  return (
    <table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">CustomerID</th>
      <th scope="col">CustomerName</th>
      <th scope="col">ContactName</th>
      <th scope="col">Country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Alfred Futterkiste</td>
      <td>Maria Anders</td>
      <td>Germany</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Ana Trujillo Emparedados y helados</td>
      <td>Ana Trujillo</td>
      <td>Mexico</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>Antonio Moreno Taqueria</td>
      <td>Antonio Moreno</td>
      <td>Mexico</td>
    </tr>
  </tbody>
</table>
  )
}

  render () {
      if (this.state.isEditorVisible == true) {
        return(
        <div>
        {this.renderEditor()}
       </div>
     )
      }
      else if (this.state.isEditorVisible == false) {
        return(
        <div>
        {this.renderMainPageContent()}
        </div>
    )
  }
}
}
export default App;
