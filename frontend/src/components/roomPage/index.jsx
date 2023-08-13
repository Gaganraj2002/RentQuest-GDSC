import React, { useState } from "react";
import "./style.css";
import axios from "axios";
import img from "./s.jpg";
import { useParams, useNavigate } from "react-router-dom";
import {
  Card,
  CardHeader,
  CardBody,
  CardFooter,
  Image,
  Stack,
  Heading,
  Text,
  Divider,
  ButtonGroup,
  HStack,
  Button,
} from "@chakra-ui/react";
import { useEffect } from "react";

const RoomPage = () => {
  var [rooms, setRooms] = useState([]);
  const id = useParams();
  console.log(id);
  const navigate = useNavigate();
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/apartments/apartments/")
      .then(function (response) {
        setRooms(response.data);
      });
  }, rooms);
  var room;
  for (let item of rooms) {
    console.log(item);
    if (item.id == id.id) {
      room = item;
    }
  }

  console.log({ room });

  if (room === undefined) {
    navigate("/");
  } else {
    return (
      <div style={{ display: "flex", justifyContent: "center" }}>
        <Card maxW="sm" align="center" id="card">
          <CardBody>
            <Image
              src={img}
              alt="Green double couch with wooden legs"
              borderRadius="lg"
            />
            <Stack mt="6" spacing="3">
              <HStack spacing="24px">
                <Heading size="md">{room.title}</Heading>
              </HStack>
              <Text>
                <b>Location: </b>
                {room.location}
              </Text>
              <Text>
                <b>Description: </b>
                {room.description}
              </Text>
              <Text color="blue.600" fontSize="2xl">
                <b>Rent: </b> {room.price} $
              </Text>
            </Stack>
          </CardBody>
          <Divider />
          <CardFooter>
            <ButtonGroup spacing="2">
              <Button variant="solid" colorScheme="blue">
                Book now
              </Button>
              <Button
                variant="ghost"
                style={{ backgroundColor: "tomato", color: "white" }}
              >
                Like
              </Button>
            </ButtonGroup>
          </CardFooter>
        </Card>
      </div>
    );
  }
};

export default RoomPage;
