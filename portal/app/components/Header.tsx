"use client";

import { AppBar, Button, Toolbar, Typography } from "@mui/material";

const Header = function (): JSX.Element {
  return (
    <AppBar position="fixed" className="h-20 flex justify-center">
      <Toolbar className="flex h-full flex-row justify-between">
        <Typography
          className="text-white"
          variant="h1"
          fontSize="large"
          fontFamily="monospace"
        >
          Properties Prices Register
        </Typography>
        <Button variant="text" href="/about" className="text-white">
          About
        </Button>
      </Toolbar>
    </AppBar>
  );
};

export default Header;
