import React from 'react';
import ReactDom from 'react-dom/client';
import { CacheProvider } from '@emotion/react';
import { ThemeProvider, CssBaseline } from '@mui/material';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { BrowserRouter } from 'react-router-dom';
import { rtlCache } from './theme/rtlCache';
import { theme } from './theme/theme';
import App from './App';
import '@fontsource/vazirmatn';

const queryClient = new QueryClient();

ReactDom.createRoot(document.getElementById('root')).render(
  <CacheProvider value={rtlCache}>
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <QueryClientProvider client={queryClient}>
        <BrowserRouter>
          <App />
        </BrowserRouter>
      </QueryClientProvider>
    </ThemeProvider>
  </CacheProvider>
);
