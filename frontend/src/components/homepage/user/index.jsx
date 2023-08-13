import "./style.css";
import axios from "axios";
import React from "react";
import Nav from "../../Nav";
import HotelCard from "../../hotelCard";
import { useEffect } from "react";
import { useState } from "react";

const User = () => {
  var [rooms, setRooms] = useState([]);
  var rooms
  useEffect(() => {
      axios.get('http://127.0.0.1:8000/api/apartments/apartments/')
        .then(function (response) {
        setRooms(response.data)
        })
    }, rooms);
  console.log(rooms)
  return (
    <>
      <div id="main">
        {console.log(rooms)}
        <div id="remaining-main-body">
          {rooms.map((item) => {
            return (
              <>
              <div style={{ marginTop: "2rem" }}>
            <HotelCard props={item} />
          </div>
              </>
            )
          })}
        
        </div>
      </div>
    </>
  );
};

export default User;
