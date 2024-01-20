"use client";

import { AppBar, Box, Button, Toolbar, Typography } from "@mui/material";
import Image from "next/image";

const Header = function (): JSX.Element {
  return (
    <AppBar position="fixed" className="h-20 flex justify-center">
      <Toolbar className="flex h-full flex-row justify-between">
        <Box className="flex flex-row gap-2 items-center">
          <Typography
            className="text-white"
            variant="h1"
            fontSize="large"
            fontFamily="monospace"
          >
            Properties Prices Register
          </Typography>
          <Image
            src="/work-in-progress.png"
            alt="logo"
            width="48"
            height="48"
          />
        </Box>
        <Box className="flex flex-row gap-2">
          <Button variant="text" href="/api" className="text-white">
            API
          </Button>
          <Button variant="text" href="/about" className="text-white">
            About
          </Button>
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Header;
