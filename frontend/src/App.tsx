import React from 'react'
import './App.css'
import { Box, Heading } from '@chakra-ui/react'

function App() {
  return (
    <React.Fragment>
      <Heading as='h1'>Crypto Tracker</Heading>
      <Box mt={4}>
        <Heading as='h2' size='lg'>
          Your portfolio
        </Heading>
      </Box>
      <Box mt={4}>
        <Heading as='h2' size='lg'>
          Assets by wallet
        </Heading>
      </Box>
    </React.Fragment>
  )
}

export default App
