import { render, screen } from '@testing-library/react';
import App from '../App';
import { QueryClient, QueryClientProvider } from "react-query";
import flaskApi from '../utils/flaskApi';
import AxiosMockAdapter from "axios-mock-adapter";

const queryClient = new QueryClient();
const axiosMock = new AxiosMockAdapter(flaskApi);
console.log('Setting up mock for /api/get');

beforeEach(() => {
  axiosMock.reset();
  axiosMock.onGet("/api/get").reply(200, "Hello from Python Backend at");
  console.log('Mock for /api/get set up successfully');
});

test('renders response', async () => {
  render(
    <QueryClientProvider client={queryClient}>
      <App />
    </QueryClientProvider>
  );
  const responseElement = screen.getByText(/response:/);
  const response = await screen.findByText(/Hello from Python Backend at/);
  expect(responseElement).toBeInTheDocument();
  expect(response).toBeInTheDocument();
});