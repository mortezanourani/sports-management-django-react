import { Outlet, Link } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Container, Box } from '@mui/material';

export default function PublicLayout() {
  return (
    <Box>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1}}>
          </Typography>
          <Link to="/" style={{ color: 'inherit', marginInlineEnd: 16 }}>ورزشکاران</Link>
          <Link to="/champions" style={{ color: 'inherit', marginInlineEnd: 16 }}>قهرمانان</Link>
          <Link to="/facilities" style={{ color: 'inherit', marginInlineEnd: 16 }}>اماکن ورزشی</Link>
          <Link to="/login" style={{ color: 'inherit' }}>ورود</Link>
        </Toolbar>
      </AppBar>
      <Container sx={{ mt: 4 }}>
        <Outlet />
      </Container>
    </Box>
  );
}
