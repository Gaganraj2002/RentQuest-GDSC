import './App.css';
import User from './components/homepage/user';
import { Login } from './components/login';
import Signup from './components/signup';
import { Route, Routes } from "react-router-dom"

function App() {
  console.log("Hello world")
  return (
   
    <div className="App">
      {/* <Nav /> */}
      <Routes>
      <Route path='/' element={<User />} />
        <Route path='/login' element={<Login />} />
        <Route path='/signup' element={<Signup />} />
      </Routes>


    </div>
  );
}

export default App;
