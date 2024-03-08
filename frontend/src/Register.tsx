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

export const Register = () => {
  const [username, setUsername] = useState<string | undefined>()
  const [password, setPassword] = useState<string | undefined>()
  const [email, setEmail] = useState<string | undefined>()
  const [firstName, setFirstName] = useState<string | undefined>()
  const [lastName, setLastName] = useState<string | undefined>()

  const handleEmailInputChange = (e) => setUsername(e.target.value)
  const handlePasswordInputChange = (e) => setPassword(e.target.value)
  const handleEmailInputChange = (e) => setEmail(e.target.value)
  const handleFirstNameInputChange = (e) => setFirstName(e.target.value)
  const handleLastNameInputChange = (e) => setLastName(e.target.value)

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
