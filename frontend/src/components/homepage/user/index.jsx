import "./style.css"

import React from 'react'
import Nav from '../../Nav'
import HotelCard from '../../hotelCard'

const User = () => {
    return (
        <>
            <Nav />
            <div id="main">
                <div id='remaining-main-body'>
                    <div style={{marginTop: "2rem"}}>
                        <HotelCard />
                    </div>
                </div>
            </div>
        </>
    )
}

export default User