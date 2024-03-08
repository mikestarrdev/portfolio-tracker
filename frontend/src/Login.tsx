import {
  Box,
  Button,
  FormControl,
  FormErrorMessage,
  FormHelperText,
  FormLabel,
  Heading,
  Input,
  Link,
  Text,
} from '@chakra-ui/react'
import { useState } from 'react'

export const Login = () => {
  const [username, setUsername] = useState<string | undefined>()
  const [password, setPassword] = useState<string | undefined>()

  const handleEmailInputChange = (e) => setUsername(e.target.value)
  const handlePasswordInputChange = (e) => setPassword(e.target.value)

  const handleLogin = (e) => {
    e.preventDefault()
  }

  const isError = username === ''
  return (
    <Box m={4} justifyContent='center'>
      <Heading as='h2' textAlign='center'>
        Login
      </Heading>
      <FormControl isInvalid={isError}>
        <FormLabel>Username</FormLabel>
        <Input
          type='text'
          placeholder='Type your username'
          value={username}
          onChange={handleEmailInputChange}
          required
        />
        {/* {isError && <FormErrorMessage>Username is required.</FormErrorMessage>} */}
        <hr />
        <FormLabel>Password</FormLabel>
        <Input
          type='password'
          placeholder='Type your password'
          value={password}
          onChange={handlePasswordInputChange}
          required
        />
        {/* {!isError ? (
          <FormHelperText>Enter password</FormHelperText>
        ) : (
          <FormErrorMessage>Password is required.</FormErrorMessage>
        )} */}
        <Button rounded='full' my={4} w='full' onClick={handleLogin}>
          Login
        </Button>
      </FormControl>
      <Text align='center'>
        Don't have an account?{' '}
        <Link href='/register' textDecoration='underline'>
          Click here to register
        </Link>
      </Text>
    </Box>
  )
}
