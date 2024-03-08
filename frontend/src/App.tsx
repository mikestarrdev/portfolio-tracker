import React from 'react'
import { Box, Heading } from '@chakra-ui/react'
import { Login } from './Login'

function App() {
  return (
    <React.Fragment>
      <Heading as='h1'>Crypto Tracker</Heading>
      <Login />
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
