import { render, screen } from '@testing-library/react';
import App from '../App';
import { QueryClient, QueryClientProvider } from "react-query";
import axios from "axios";
import AxiosMockAdapter from "axios-mock-adapter";

const queryClient = new QueryClient();
const axiosMock = new AxiosMockAdapter(axios);

beforeEach(() => {
  axiosMock.reset();
  axiosMock.onGet("/api/get").reply(200, {data: "Hello from Python Backend at"});
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