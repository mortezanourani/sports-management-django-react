import { Outlet, Link } from 'react-router-dom';
import { Box, Drawer, List, ListItemButton, Toolbar, AppBar, Typography } from '@mui/material';

const drawerWidth = 240;

export default function DashboardLayout() {
  return (
    <Box sx={{ display: 'flex' }}>
      <AppBar position="fixed" sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}>
        <Toolbar>
          <Typography variant="h6">پنل مدیریت</Typography>
        </Toolbar>
      </AppBar>
      <Drawer
        variant="permanent"
        anchor="right"
        sx={{ width: drawerWidth, flexShrink: 0, '& .MuiDrawer-paper': { width: drawerWidth } }}
      >
        <Toolbar />
        <List>
          <ListItemButton component={Link} to="/dashboard/facilities">
            <ListItemText primary="اماکن ورزشی" />
          </ListItemButton>
          <ListItemButton component={Link} to="/dashboard/champions">
            <ListItemText primary="مدال آوران" />
          </ListItemButton>
          <ListItemButton component={Link} to="/dashboard/federations">
            <ListItemText primary="هیات های ورزشی" />
          </ListItemButton>
          <ListItemButton component={Link} to="/dashboard/athletes">
            <ListItemText primary="آمار ورزشکاران" />
          </ListItemButton>
          <ListItemButton component={Link} to="/dashboard/messages">
            <ListItemText primary="پبام ها" />
          </ListItemButton>
        </List>
      </Drawer>
      <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
        <Toolbar />
        <Outlet />
      </Box>
    </Box>
  );
}
