"use client";

import { AppBar, Box, Button, Toolbar, Typography } from "@mui/material";
import Image from "next/image";
import Link from "next/link";

const Header = function (): JSX.Element {
  return (
    <AppBar
      position="fixed"
      className="h-14 flex justify-center bg-emerald-800"
    >
      <Toolbar className="flex h-full flex-row justify-between">
        <Box className="flex flex-row gap-2 items-center">
          <Link href="/">
            <Typography className="text-white" textTransform="uppercase">
              Catchy Name
            </Typography>
          </Link>
          <Image
            src="/work-in-progress.png"
            alt="logo"
            width="48"
            height="48"
          />
        </Box>
        <Box className="flex flex-row gap-2">
          <Link href="/api">
            <Button variant="text" className="text-white">
              API
            </Button>
          </Link>
          <Link href="/about">
            <Button variant="text" className="text-white">
              About
            </Button>
          </Link>
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Header;
