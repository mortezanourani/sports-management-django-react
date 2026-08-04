import { Routes, Route } from 'react-router-dom';
import PublicLayout from './layouts/PublicLayout';
import DashboardLayout from './layouts/DashboardLayout';
import ProtectedRoute from './components/ProtectedRoute';
import AthleteStats from './pages/public/AthleteStats';
import ChampionStats from './pages/public/ChampionStats';
import FacilityStats from './pages/public/FacilityStats';
import Login from './pages/auth/Login';
import FacilitiesList from './pages/dashboard/Facilities/FacilitiesList';

export default function App() {
  return (
    <Routes>
      <Route element={<PublicLayout />}>
        <Route path="/" element={<AthleteStats />} />
        <Route path="/champions" element={<ChampionStats />} />
        <Route path="/facilities" element={<FacilityStats />} />
      </Route>

      <Route path="/login" element={<Login />} />

      <Route element={<ProtectedRoute />}>
        <Route element={<DashboardLayout />}>
          <Route path="/dashboard/facilities" element={<FacilitiesList />} />
        </Route>
      </Route>
    </Routes>
  );
}

