import { Typography } from "@mui/material";
import Image from "next/image";

export default function Home() {
  return (
    <main className="flex w-full h-full flex-row justify-center items-center">
      <Image
        src="/coming-soon.png"
        alt="coming soon"
        width="128"
        height="128"
      />
    </main>
  );
}
