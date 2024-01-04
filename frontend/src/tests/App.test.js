import { render, screen } from '@testing-library/react';
import App from '../App';
import { QueryClient, QueryClientProvider } from "react-query";
import flaskApi from '../utils/flaskApi';
import AxiosMockAdapter from "axios-mock-adapter";

const queryClient = new QueryClient();
const axiosMock = new AxiosMockAdapter(flaskApi);
console.log('Setting up mock for /get');

beforeEach(() => {
  axiosMock.reset();
  axiosMock.onGet("/get").reply(200, {"message": "Hello from Python Backend at"});
  console.log('Mock for /get set up successfully');
});

test('renders response', async () => {
  render(
    <QueryClientProvider client={queryClient}>
      <App />
    </QueryClientProvider>
  );
  const responseElement = screen.getByText(/This website is currently under development. Please check back later for updates./);
  expect(responseElement).toBeInTheDocument();
});