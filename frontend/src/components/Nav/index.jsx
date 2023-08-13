import "./style.css"
import {useNavigate} from "react-router-dom"
import React from 'react'

const Nav = () => {
    const navigate = useNavigate()
  return (
    <>
        <div id="nav">
            <div id="logo" onClick={() => navigate("/")}>RentQuest</div>
            <div id="menu">
                <ol>
                    <li>
                        <input placeholder="Search...." id="search-box" type="text" />
                    </li>
                    <li>Profile</li>
                    <li>Log Out</li>
                </ol>
            </div>
        </div>
    </>
  )
}

export default Nav