//// the code for calculator wont work. to make it work, copy the return part fom Calculator.js and paste it where we have called <Calculator />

import React, {Component} from "react";
import ReactDOM from 'react-dom';
import {BrowserRouter as Router, Route, Redirect} from "react-router-dom";
import DummyPage from './dummyPage';
import AppRouter from './router';
class App extends Component {
    state = { value: 0,
             array: [1,2,3,4,5],
             userChoice: 0,
             firstNumber: 0,
             secondNumber: 0,
             finalResult: 0,
             button1: 1,
             button2: 2,
             button3: 3,
             button4: 4,
             button5: 5,
             button6: 6,
             button7: 7,
             button8: 8,
             button9: 9,
             user1: true,
             user2: false,
             todoList: [ ],
             currentTodo: "",
             todoItemToBeUpdated: "",
             updatedTodoValue: "",
             userName: "",
             password: "",
             registeredUsers: [],
             userToBeDeleted: ""
            }

    renderCurrentUserArea() {

        if (this.state.user1 == true) {
            return (
                <div>
                    <br />
                    Its your turn user1
                 </div>
            )
        } else if (this.state.user2 == true) {
            return (
                 <div>
                    <br />
                    Its your turn user2
                 </div>
            )
        }
    }

    componentDidMount() {
      this.makeRequest()
    }

    navigateToPage = event => {
      return <AppRouter />
    }

    handleUserName = event => {
        this.setState({userName: event.target.value});
    }

    handlePassword = event => {
        this.setState({password: event.target.value})
    }

    handleUserToBeDeleted = event => {
      this.setState({userToBeDeleted: event.target.value});
    }

    makeDeleteRequest = event => {
      let localhostUrl = 'http://localhost:5454/posts/'
      let userToBeDeleted = this.state.userToBeDeleted.toString()
      let filteredUser = this.state.registeredUsers.filter(function(userObject){
         return userObject.title == userToBeDeleted
      })
      let filteredUserObjectId = filteredUser[0].id.toString()

      let completeUrl = localhostUrl + filteredUserObjectId
      fetch(completeUrl, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json'
        }
      })
    }

    submitForm = event => {
      let jsonDummyData = JSON.stringify({
        title: this.state.userName,
        tags: this.state.password
      })

      fetch('http://localhost:5454/posts', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: jsonDummyData
      })
      .then(res => res.json())
    }

    renderWinnerArea() {
          if ((this.state.button1 == "X" && this.state.button2 == "X" && this.state.button3 == "X")) {
            return (
                <p> The winner is user1 </p>
            )
        } else if ((this.state.button1 == "O" && this.state.button2 == "O" && this.state.button3 == "O")) {
            return (
                <p> The winner is user2 </p>
            )
        } else if (this.state.button1 == "X" && this.state.button4 == "X" && this.state.button7 == "X") {
            return (
                <p> The winner is user1 </p>
            )
        } else if (this.state.button1 == "O" && this.state.button4 == "O" && this.state.button7 == "O") {
            return (
                <p> The Winner is user2 </p>
            )
        } else if (this.state.button4 == "X" && this.state.button5 == "X" && this.state.button6 == "X") {
            return (
                <p> The winner is user1 </p>
            )
        } else if (this.state.button7 == "X" && this.state.button8 == "X" && this.state.button9 == "X") {
            return (
                <p> The winner is user1 </p>
            )
        } else if (this.state.button4 == "O" && this.state.button5 == "O" && this.state.button6 == "O") {
            return (
                <p> The winner is user2 </p>
            )
        } else if (this.state.button7 == "O" && this.state.button8 == "O" && this.state.button9 == "O") {
            return (
                <p> The winner is user2 </p>
            )
        } else if (this.state.button2 == "X" && this.state.button5 == "X" && this.state.button8 == "X") {
            return (
                <p> The winner is user1 </p>
            )
        } else if (this.state.button3 == "X" && this.state.button6 == "X" && this.state.button9 == "X") {
            return (
                <p> The winner is user1 </p>
            )
        } else if (this.state.button2 == "O" && this.state.button5 == "O" && this.state.button8 == "O") {
            return (
                <p> the winner is user2 </p>
            )
        } else if (this.state.button3 == "O" && this.state.button6 == "O" && this.state.button9 == "O") {
            return (
                <p> The winner is user2 </p>
            )
        } else if (this.state.button1 == "X" && this.state.button5 == "X" && this.button9 == "X") {
            return (
                <p> The winner is user1 </p>
            )
        } else if (this.state.button3 == "X" && this.state.button5 == "X" && this.state.button7 == "X") {
            return (
                <p> The winner is user1 </p>
            )
        } else if (this.state.button1 == "O" && this.state.button5 == "O" && this.button9 == "O") {
            return (
                <p> the winner is user2 </p>
            )
        } else if (this.state.button3 == "O" && this.state.button5 == "O" && this.state.button7 == "O") {
            return (
                <p> the winner is user2 </p>
            )
        }
    }
    handleButton1Change = event => {
        if (this.state.user1 == true) {
         this.setState({button1: "X", user1: false, user2: true});
        } else if (this.state.user2 == true) {

            this.setState({button1: "O", user1: true, user2: false});
        }
    }

    handleButton2Change = event => {
        if (this.state.user1 == true) {
            this.setState({button2: "X", user1: false, user2: true})
        } else if (this.state.user2 == true) {
            this.setState({button2: "O", user1: true, user2: false});
        }
    }

    handleButton3Change = event => {
        if (this.state.user1 == true) {
            this.setState({button3: "X", user1: false, user2: true})
        } else if (this.state.user2 == true) {
            this.setState({button3: "O", user1: true, user2: false});
        }
    }

    handleButton4Change = event => {
        if (this.state.user1 == true) {
            this.setState({button4: "X", user1: false, user2: true})
        } else if (this.state.user2 == true) {
            this.setState({button4: "O", user1: true, user2: false});
        }
    }

    handleButton5Change = event => {
        if (this.state.user1 == true) {
            this.setState({button5: "X", user1: false, user2: true})
        } else if (this.state.user2 == true) {
            this.setState({button5: "O", user1: true, user2: false});
        }
    }

    handleButton6Change = event => {
        if (this.state.user1 == true) {
            this.setState({button6: "X", user1: false, user2: true})
        } else if (this.state.user2 == true) {
            this.setState({button6: "O", user1: true, user2: false});
        }
    }

    handleButton7Change = event => {
        if (this.state.user1 == true) {
            this.setState({button7: "X", user1: false, user2: true})
        } else if (this.state.user2 == true) {
            this.setState({button7: "O", user1: true, user2: false});
        }
    }

    handleButton8Change = event => {
        if (this.state.user1 == true) {
            this.setState({button8: "X", user1: false, user2: true})
        } else if (this.state.user2 == true) {
            this.setState({button8: "O", user1: true, user2: false});
        }
    }

    handleButton9Change = event => {
        if (this.state.user1 == true) {
            this.setState({button9: "X", user1: false, user2: true})
        } else if (this.state.user2 == true) {
            this.setState({button9: "O", user1: true, user2: false});
        }
    }

    handleChange = event => {
        this.setState({value: event.target.value});
    }

    performAddition = event => {
        let updatedFinalResult = Number(this.state.firstNumber) + Number(this.state.secondNumber )
        this.setState({finalResult: updatedFinalResult});
    }

    performSubtraction = event => {
        let firstNumber = Number(this.state.firstNumber)
        let secondNumber = Number(this.state.secondNumber)
        if (firstNumber > secondNumber) {
            this.setState({finalResult: (firstNumber - secondNumber)});
        } else {
            this.setState({finalResult: (secondNumber - firstNumber)});
        }

    }

    performDivision = event => {
        let firstNumber = Number(this.state.firstNumber)
        let secondNumber = Number(this.state.secondNumber)

        if (firstNumber > secondNumber) {
            this.setState({finalResult: (firstNumber / secondNumber)});
        } else {
            this.setState({finalResult: (secondNumber / firstNumber)});
        }
    }

    performMultiplication = event => {
        this.setState({finalResult: (Number(this.state.firstNumber) * Number(this.state.secondNumber))});
    }

    addValue = event => {
        let incrementedValue = Number(this.state.value + 1)
        this.setState({value:  incrementedValue});
    }

    subtractValue = event => {
        let decrementedValue = Number(this.state.value - 1)
        this.setState({value: decrementedValue});
    }

    handleUserChoice1 = event => {
        this.setState({userChoice: 1});
    }

    handleUserChoice2 = event => {
        this.setState({userChoice: 2});
    }

    handleChangeForFirstNumber = event => {
        this.setState({firstNumber: event.target.value});
    }

    handleChangeForSecondNumber = event => {
        this.setState({secondNumber: event.target.value});
    }

    renderTicTacToe = event => {
        this.setState({userChoice: 4});
    }

    renderTodo = event => {
        this.setState({userChoice: 5});
    }

    renderForm = event => {
        this.setState({userChoice: 6});
    }

    renderDeleteRequestArea = event => {
      this.setState({userChoice: 7})
    }

    modifyArray = event => {
        const arr = this.state.array
        const updatedArray = arr.map((arrayValue) =>
            <li> {arrayValue * 2} </li>
        );
        return updatedArray

    }

    refreshScreen = event => {
        this.setState({userChoice: -10});
    }

    renderCalculator = event => {
        this.setState({userChoice: 3});
    }

    handleCurrentTodo = event => {
        this.setState({currentTodo: event.target.value});
    }



    addTodo = event => {
        let todoList = this.state.todoList
        let currentTodo = this.state.currentTodo
        this.setState({todoList: todoList.concat([currentTodo])})
    }

    deleteTodo = (todoItem) => {
        let todoList = this.state.todoList
        this.setState({todoList: (todoList.filter(function(todo){
            return todo != todoItem
        }))})
    }


    renderEditableTodoComponent = (todoItem) => {
        let todoList = this.state.todoList
        todoList.map((todo) =>
            (todo != todoItem) ? <p> True </p> : <p> False </p>
            ) }

    updateTodoItem = (todo) => {
        this.setState({todoItemToBeUpdated: todo})
    }

    renderEditableTodo = (todo) => {
        let todoItem  = this.state.todoItemToBeUpdated
        return ( todoItem != todo ? this.renderEditableTodoComponent(todo) : <div> </div>
        )
    }

    renderAddedTodosArea = event => {
        return this.state.todoList.map((todo) =>
                <div>
               <li> {todo} {" "}
                {" "}
                <input type = "button" value = "Delete Todo" onClick = {() => this.deleteTodo({todo})} />
                {" "}
                <input type = "button" value = "Edit Todo" onClick = {() => this.updateTodoItem({todo})} />

                {" "}
                {this.renderEditableTodo(todo)}
                </li>
                <br />
                </div>
        );

    }

    makeRequest = event => {
       let registeredUsers = this.state.registeredUsers

        fetch('http://localhost:5454/posts'
        )
        .then(resp => resp.json())
        .then(data => this.setState({registeredUsers: data}))

    }

    handleNavigationChoice = event => {
      this.setState({userChoice: 8})
    }

    renderhtmlForUserChoice(){
        if (this.state.userChoice == 1) {
            return (
                <div>
            <br />
            <input type="button"
             value= "+"
              onClick = {this.addValue} />
            {" "}
            <input
             type="text"
             value = {this.state.value}
             onChange = {this.handleChange} />
            {" "}
            <input type="button"
             value=  "-"//{this.state.value}
             onClick = {this.subtractValue} />

            </div>
            )

        } else if (this.state.userChoice == 2) {
            return (
                <div>
                 initial Array: <br /> [1,2,3,4,5]
                  <br />
                 doubled Array :
                     <div>
                        {this.modifyArray()}
                     </div>
                </div>
            )

        } else if (this.state.userChoice == -10 || this.state.userChoice > 8) {
            return (<p> </p>)

        } else if (this.state.userChoice == 3) {
                return (
                    <div>
                    <input
                        type = "text"
                        value = {this.state.firstNumber}
                        onChange = {this.handleChangeForFirstNumber} />
                    <br />
                    <input
                        type = "text"
                        value = {this.state.secondNumber}
                        onChange = {this.handleChangeForSecondNumber} />
                    <br />
                    <input
                        readOnly
                        value = {this.state.finalResult}
                        />
                    < br />
                     <input
                        type = "button"
                        value = "+"
                        onClick = {this.performAddition} />
                    {" "}
                     <input
                        type = "button"
                        value = "-"
                        onClick = {this.performSubtraction} />
                    {" "}
                      <input
                        type = "button"
                        value = "/"
                        onClick = {this.performDivision} />
                    {" "}
                      <input
                        type = "button"
                        value = "*"
                        onClick = {this.performMultiplication} />
                 </div>
                )
        } else if (this.state.userChoice == 4) {
            return (
              <div>
                <div>
                 <input
                    type = "button"
                    value = {this.state.button1}
                    onClick = {this.handleButton1Change} />
                <input
                    type = "button"
                    value = {this.state.button2}
                    onClick = {this.handleButton2Change} />
                <input
                    type = "button"
                    value = {this.state.button3}
                    onClick = {this.handleButton3Change} />
                <br />
                 <input
                    type = "button"
                    value = {this.state.button4}
                    onClick = {this.handleButton4Change} />
                <input
                    type = "button"
                    value = {this.state.button5}
                    onClick = {this.handleButton5Change} />
                <input
                    type = "button"
                    value = {this.state.button6}
                    onClick = {this.handleButton6Change} />
                <br />
                <input
                    type = "button"
                    value = {this.state.button7}
                    onClick = {this.handleButton7Change} />

                <input
                    type = "button"
                    value = {this.state.button8}
                    onClick = {this.handleButton8Change} />

                <input
                    type = "button"
                    value = {this.state.button9}
                    onClick = {this.handleButton9Change} />

                <div>
                  {this.renderCurrentUserArea()}
                </div>

                <div>
                    {this.renderWinnerArea()}
                </div>

                </div>
                </div>
            )
        } else if (this.state.userChoice == 5) {
            return (
                <div>
                    <input
                        type = "text"
                        value = {this.state.currentTodo}
                        onChange = {this.handleCurrentTodo} />
                    {" "}
                    <input
                        type = "button"
                        value = "Add Todo"
                        onClick = {this.addTodo} />
                     {" "}
                    <br />
                    <p> TODO'S </p>
                    <br />

                    <div>
                        {this.renderAddedTodosArea()}
                    </div>
                </div>
            )
        } else if (this.state.userChoice == 6) {
            return (
                <div>
                    <input type = "text" value= {this.state.userName} onChange = {this.handleUserName}/>
                    <br />
                    <input type = "text" value = {this.state.password} onChange ={this.handlePassword} />
                    <br />
                    <input type = "button" value = "Submit" onClick = {this.submitForm} />
                </div>
            )
        } else if (this.state.userChoice == 7) {
          return (
            <div>
             <br />
             {" "}
              <input type = "text" value = {this.state.userToBeDeleted} onChange = {this.handleUserToBeDeleted} />
              {" "}
              <br />
              <input type = "button" value = "Delete" onClick = {this.makeDeleteRequest} />
             </div>

          )
        } else if (this.state.userChoice == 8) {
          return (
            <div>
                {this.navigateToPage()}
            </div>
          )
        }
    }
    render() {
        return (
            <div>

            <div>
             Click on the button of your choice. Enjoy! : ) <br />

            <input
              type = "button"
              value = "+ - game "
              onClick = {this.handleUserChoice1} />
            {" "}
             <input
               type= "button"
               value= "array updation"
               onClick = {this.handleUserChoice2} />
            {" "}
                <input
                    type = "button"
                    value = "Open Calculator"
                    onClick = {this.renderCalculator} />
            {" "}
              <input
                type = "button"
                value = "Tic Tac Toe"
                onClick = {this.renderTicTacToe} />
            {" "}
                <input
                 type = "button"
                 value = "Todo"
                 onClick = {this.renderTodo} />
            {" "}
                <input
                 type = "button"
                 value = "Make GET request"
                 onClick = {this.makeRequest} />
            {" "}
                <input
                 type = "button"
                 value = "Open Form"
                 onClick = {this.renderForm} />
            {" "}
                <input
                  type = "button"
                  value = "Navigate"
                  onClick = {this.handleNavigationChoice} />
            {" "}
             <input
                type = "button"
                value = "Refresh screen"
                onClick = {this.refreshScreen} />

            {" "}
              <input
                type = "button"
                value = "Make Delete Request"
                onClick = {this.renderDeleteRequestArea} />
            </div>

            <div>
             {this.renderhtmlForUserChoice()}
            </div>

            </div>

        )
    }
}
ReactDOM.render(<App />,document.getElementById('root'));
export default App;
