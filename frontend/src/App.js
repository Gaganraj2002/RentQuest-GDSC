import './App.css';
import { Login } from './components/login';
import Signup from './components/signup';
// import { Nav } from './components/navigation';
import { Route, Routes } from "react-router-dom"

function App() {
  return (
    <div className="App">
      <Nav />
      <Routes>
        <Route path='/login' element={<Login />} />
        <Route path='/signup' element={<Signup />} />
      </Routes>


    </div>
  );
}

export default App;
