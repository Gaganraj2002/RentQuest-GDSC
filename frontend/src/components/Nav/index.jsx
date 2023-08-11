import "./style.css"

import React from 'react'

const Nav = () => {
  return (
    <>
        <div id="nav">
            <div id="logo">RentQuest</div>
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