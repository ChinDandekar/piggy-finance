import { render} from '@testing-library/react';
import App from '../App';
import { QueryClient, QueryClientProvider } from "react-query";
import flaskApi from '../utils/flaskApi';
import AxiosMockAdapter from "axios-mock-adapter";

const queryClient = new QueryClient();
const axiosMock = new AxiosMockAdapter(flaskApi);
console.log('Setting up mock for /get');

beforeEach(() => {
  axiosMock.reset();
  axiosMock.onGet("/get").reply(200, {"isLoggedIn": false});
  console.log('Mock for /get set up successfully');
});

test('renders response', async () => {
  render(
    <QueryClientProvider client={queryClient}>
      <App />
    </QueryClientProvider>
  );
});